"""Build the Vietnamese speaking manuscript as a searchable, bookmarked PDF.

Run: python -m src.build_speech_pdf
Requires reportlab and Arial on Windows, or DejaVu Sans on Linux.
The scientific experiment is not rerun by this editorial/export command.
"""
import argparse
import html
import json
from pathlib import Path
import re

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import Paragraph, Table, TableStyle

ROOT=Path(__file__).resolve().parents[1]
W,H=A4
L=51
R=W-51
CW=R-L
TOP=777
BOTTOM=57
INK=colors.HexColor("#173340")
TEAL=colors.HexColor("#006D69")
MUTED=colors.HexColor("#526D78")
PALE=colors.HexColor("#EDF5F4")
LINE=colors.HexColor("#D5E2E3")
AMBER=colors.HexColor("#A94F25")
TOTAL=32


def clean(text):
    return re.sub("[\u2010-\u2015]", "-", text)


def escape(text):
    return html.escape(clean(str(text)))

def math_fallback(text):
    # Arial on Windows omits the set-membership glyph. Embed a Unicode symbol
    # font explicitly so the formula remains visible and text-extractable.
    return text.replace("∈",'<font name="MathSymbols">∈</font>')


def register_fonts(font_dir=None):
    candidates=[]
    if font_dir:
        candidates.append((Path(font_dir),["arial.ttf","arialbd.ttf","ariali.ttf","arialbi.ttf"]))
        candidates.append((Path(font_dir),["DejaVuSans.ttf","DejaVuSans-Bold.ttf","DejaVuSans-Oblique.ttf","DejaVuSans-BoldOblique.ttf"]))
    candidates.extend([
        (Path("C:/Windows/Fonts"),["arial.ttf","arialbd.ttf","ariali.ttf","arialbi.ttf"]),
        (Path("/usr/share/fonts/truetype/dejavu"),["DejaVuSans.ttf","DejaVuSans-Bold.ttf","DejaVuSans-Oblique.ttf","DejaVuSans-BoldOblique.ttf"]),
    ])
    for directory,names in candidates:
        if all((directory/n).is_file() for n in names):
            for family,name in zip(["Body","BodyBold","BodyItalic","BodyBoldItalic"],names):
                pdfmetrics.registerFont(TTFont(family,str(directory/name)))
            pdfmetrics.registerFontFamily("Body",normal="Body",bold="BodyBold",italic="BodyItalic",boldItalic="BodyBoldItalic")
            symbol=Path("C:/Windows/Fonts/seguisym.ttf")
            if not symbol.is_file():
                symbol=directory/names[0]
            pdfmetrics.registerFont(TTFont("MathSymbols",str(symbol)))
            return
    raise FileNotFoundError("Cần bộ font Arial hoặc DejaVu Sans. Dùng --font-dir để chỉ thư mục font.")


class Manuscript:
    def __init__(self,destination):
        destination.parent.mkdir(parents=True,exist_ok=True)
        self.canvas=Canvas(str(destination),pagesize=A4,pageCompression=1)
        self.canvas.setTitle("DS111 - Bản thuyết trình đầy đủ về điền khuyết dữ liệu")
        self.canvas.setAuthor("DS111 Seminar")
        self.canvas.setCreator("DS111 Seminar - Vietnamese speaking manuscript")
        self.canvas.setSubject("24 slide: lời thoại, giải thích thuật ngữ và cơ sở toán học Mean, Median, Mode.")
        self.page=0
        self.bounds=[]
        self.page_checks=[]

    def start(self,kind,title,key=None):
        self.page+=1
        self.kind=kind
        c=self.canvas
        c.setFillColor(TEAL)
        c.rect(0,H-11,W,11,fill=1,stroke=0)
        c.setFont("BodyBold",8)
        c.drawString(L,H-34,"DS111  /  PHÂN TÍCH DỮ LIỆU")
        c.setFont("Body",8)
        c.setFillColor(MUTED)
        c.drawRightString(R,H-34,kind)
        c.setStrokeColor(LINE)
        c.line(L,43,R,43)
        c.setFont("Body",8)
        c.drawString(L,29,"Mean, Median, Mode | Bản lời thoại đầy đủ")
        c.drawRightString(R,29,f"{self.page:02} / {TOTAL}")
        if key:
            c.bookmarkPage(key)
            c.addOutlineEntry(clean(title),key,level=0,closed=False)
        self.y=TOP

    def para(self,text,size=11.25,leading=16.2,color=INK,bold=False,after=8,raw=False,x=L,width=CW):
        value=math_fallback(text if raw else escape(text))
        style=ParagraphStyle("p",fontName="BodyBold" if bold else "Body",fontSize=size,
                             leading=leading,textColor=color,alignment=TA_LEFT,
                             splitLongWords=False,allowWidows=0,allowOrphans=0)
        paragraph=Paragraph(value,style)
        _,height=paragraph.wrap(width,H)
        if self.y-height<BOTTOM:
            raise ValueError(f"Page {self.page}, {self.kind}: overflow at y={self.y:.1f}, h={height:.1f}: {text[:80]}")
        paragraph.drawOn(self.canvas,x,self.y-height)
        self.bounds.append({"page":self.page,"x":x,"top":self.y,"bottom":self.y-height,
                            "width":width,"text":clean(re.sub("<[^>]*>","",text))})
        self.y-=height+after
        return height

    def label(self,text):
        self.para(text,size=8.3,leading=11,color=TEAL,bold=True,after=5)

    def title(self,title,kicker=None):
        if kicker:
            self.para(kicker,size=9.2,leading=12,color=TEAL,bold=True,after=8)
        self.para(title,size=21,leading=26,bold=True,after=14)

    def box(self,text,title=None,size=9.6,leading=13.8,fill=PALE):
        pieces=[]
        if title:
            pieces.append(f'<b>{escape(title)}</b><br/>')
        pieces.append(text)
        p=Paragraph(math_fallback("".join(pieces)),ParagraphStyle("box",fontName="Body",fontSize=size,leading=leading,textColor=INK))
        _,height=p.wrap(CW-24,H)
        total=height+20
        if self.y-total<BOTTOM:
            raise ValueError(f"Page {self.page}: box overflow {title}")
        self.canvas.setFillColor(fill)
        self.canvas.roundRect(L,self.y-total,CW,total,7,fill=1,stroke=0)
        p.drawOn(self.canvas,L+12,self.y-height-10)
        self.bounds.append({"page":self.page,"x":L,"top":self.y,"bottom":self.y-total,"width":CW,
                            "text":clean(re.sub("<[^>]*>","",text))})
        self.y-=total+11

    def finish(self):
        self.page_checks.append({"page":self.page,"kind":self.kind,"last_y":self.y})
        self.canvas.showPage()

    def save(self):
        assert self.page==TOTAL,self.page
        self.canvas.save()


FORMULAS={
4:"x̄ = (1/n) Σ<sub>i=1</sub><super>n</super> x<sub>i</sub>",
5:"n lẻ: x<sub>((n+1)/2)</sub>.<br/>n chẵn: [x<sub>(n/2)</sub> + x<sub>(n/2+1)</sub>]/2.",
6:"Modes(X) = arg max<sub>v</sub> Count(v)",
7:"a* ∈ arg min<sub>a</sub> E[L(X,a) | M=0]<br/>â ∈ arg min<sub>a</sub> Σ<sub>i:Mᵢ=1</sub> L(x<sub>i</sub>,a)",
8:"E[(X-a)<super>2</super>] = Var(X) + (μ-a)<super>2</super><br/>f′(a) = 2na - 2Σx<sub>i</sub> = 0; suy ra a = x̄.",
9:"g(a) = Σ|x<sub>i</sub>-a|.<br/>m là trung vị nếu P(X≤m)≥1/2 và P(X≥m)≥1/2.",
10:"Σ 1(x<sub>i</sub>≠a) = n - Count(a)<br/>E[1(X≠a)] = 1 - P(X=a).",
14:"Mô hình tuyến tính cố định: Δŷ = β<sub>j</sub>(â<sub>j</sub>-x<sub>j</sub>).",
16:"s<super>2</super><sub>sau</sub> = s<super>2</super><sub>quan sát</sub> × (n-1)/(n+m-1).",
}


def slide_page(book,item):
    n=item["slide"]
    book.start(f"SLIDE {n:02}",item["title"],f"slide-{n}")
    book.title(item["title"],f"SLIDE {n:02}  |  {item['timing']}  |  MỐC GIỜ GỢI Ý")
    book.box(escape(item["cue"]),title="Chỉ hình và nhịp trình bày",size=9,leading=12.4)
    if n in FORMULAS:
        book.box(FORMULAS[n],title="Công thức đọc cùng slide",size=10.4,leading=15.2)
    book.label("LỜI THOẠI")
    for paragraph in item["speech"].split("\n\n"):
        book.para(paragraph)
    book.label("CHUYỂN Ý")
    book.para(item["transition"],size=10.5,leading=14.7,color=TEAL,after=11)
    terms="<br/>".join(f"<b>{escape(term)}:</b> {escape(definition)}" for term,definition in item["terms"])
    book.box(terms,title="Học thuật để chuẩn bị",size=9,leading=12.4,fill=colors.HexColor("#F3F5F6"))
    book.finish()


def cover(book,payload):
    book.start("BẢN BIÊN TẬP LỜI NÓI","Bìa","cover")
    book.y=737
    book.para("BẢN THUYẾT TRÌNH",size=11,leading=16,color=TEAL,bold=True,after=16)
    book.para("Điền khuyết dữ liệu<br/>bằng Mean,<br/>Median và Mode",size=34,leading=42,bold=True,after=23,raw=True)
    book.para("Từ một giá trị đại diện đến lựa chọn có căn cứ",size=15,leading=22,color=MUTED,after=31)
    book.box("Vì sao một đại diện có thể ước lượng ô thiếu?<br/>"
             "Khi nào sự thay thế đó hợp lý?<br/>"
             "Dữ liệu và mô hình sau điền thay đổi ra sao?",
             title="Ba câu hỏi xuyên suốt",size=12,leading=20)
    book.y-=14
    book.para("24 slide | Lời thoại hoàn chỉnh | Giải thích học thuật",size=11.2,leading=17,bold=True,after=14)
    book.para("Dữ liệu thực tế: UCI Student Performance, 649 quan sát.<br/>"
              "Kết quả có kiểm chứng từ thí nghiệm khôi phục ô thiếu và<br/>"
              "370 lần fit Ridge / Random Forest.",size=11,leading=17,color=MUTED,raw=True)
    book.y-=19
    book.para("Bản đầy đủ để tập nói và chuẩn bị phản biện. Lời thoại bám 24 slide của bộ trình chiếu; phần học thuật và phụ lục dùng để ôn tập.",size=10.5,leading=16,color=MUTED)
    book.finish()


def contents(book,payload):
    book.start("CÁCH DÙNG","Mục lục và cách dùng","contents")
    book.title("Mục lục và cách dùng")
    book.para("Mỗi slide có lời thoại, câu chuyển ý và ghi chú học thuật. Khi tập, đọc phần lời thoại và chuyển ý; dùng ghi chú để hiểu công thức và trả lời câu hỏi.",size=10.5,leading=15)
    book.box("Bản 24 slide cần khoảng 25 phút trình bày; các mốc giờ là gợi ý và cần tập có bấm giờ. "
             "Với seminar 15 phút, dùng lộ trình 13 slide đã chọn và lời thoại rút gọn trong project.",
             title="Thời lượng",size=9.4,leading=13.4)
    book.y-=2
    c=book.canvas
    for item in payload["slides"]:
        n=item["slide"]
        y=book.y
        text=f"{n:02}   {item['title']}"
        book.para(text,size=10.3,leading=13.3,after=3,width=CW-32)
        c.setFont("Body",9.2)
        c.setFillColor(MUTED)
        c.drawRightString(R,y-10.3,str(n+2))
        c.linkAbsolute("",f"slide-{n}",(L,book.y,R,y),thickness=0)
    book.y-=8
    for label,key,page in [
        ("Phụ lục A-B: Cơ sở toán học và điều kiện áp dụng","math-1",27),
        ("Phụ lục C-D: Thuật ngữ để ôn tập","glossary-1",29),
        ("Phụ lục E: Bảng kết quả và câu hỏi thường gặp","qa",31),
        ("Nguồn, phạm vi và cách kiểm tra số liệu","sources",32)]:
        y=book.y
        book.para(label,size=9.6,leading=13.2,after=4,width=CW-32,color=TEAL)
        c.setFont("Body",9.2);c.drawRightString(R,y-10.3,str(page))
        c.linkAbsolute("",key,(L,book.y,R,y),thickness=0)
    book.finish()


def math_pages(book):
    book.start("PHỤ LỤC A","Cơ sở toán học: mục tiêu và Mean","math-1")
    book.title("Từ mục tiêu điền đến nghiệm Mean")
    book.para("Phần này dùng để học và trả lời phản biện; không cần đọc nguyên văn khi thuyết trình.",size=10,leading=15,color=MUTED,after=14)
    book.label("1. MỤC TIÊU TRÊN PHẦN THIẾU")
    book.box("a* ∈ arg min<sub>a</sub> E[L(X,a) | M=0]<br/>"
             "â ∈ arg min<sub>a</sub> (1/n<sub>obs</sub>) Σ<sub>i:Mᵢ=1</sub>L(x<sub>i</sub>,a)",
             size=12,leading=20)
    book.para("M=1 là quan sát, M=0 là thiếu. Công thức đầu là đích dự đoán; công thức sau học từ mẫu quan sát. Muốn chuyển nghiệm sang phần thiếu, cần giả định đại diện phù hợp. Dưới MCAR, X độc lập với M nên phân phối X|M=0 và X|M=1 bằng nhau theo mô hình. Sai số lấy mẫu vẫn tồn tại.")
    book.label("2. MEAN TỐI ƯU RỦI RO BÌNH PHƯƠNG")
    book.para("Gọi μ=E[X] và giả sử E[X²] hữu hạn. Viết X-a=(X-μ)+(μ-a), khai triển rồi lấy kỳ vọng:")
    book.box("E[(X-a)<super>2</super>]<br/>"
             "= E[(X-μ)<super>2</super>] + 2(μ-a)E[X-μ] + (μ-a)<super>2</super><br/>"
             "= Var(X) + (μ-a)<super>2</super>.",size=12,leading=21)
    book.para("Số hạng chéo bằng 0 vì E[X-μ]=0. Var(X) cố định theo a, nên chọn a=μ làm rủi ro nhỏ nhất. Trên mẫu, f(a)=Σ(xᵢ-a)² có f′(a)=2na-2Σxᵢ và f″(a)=2n>0. Nghiệm duy nhất là x̄.")
    book.box("Nghiệm tối ưu vẫn để lại rủi ro Var(X). Một dự đoán hằng số tối ưu không xác định chắc chắn giá trị riêng của người có ô thiếu.",title="Ý nghĩa khi trình bày",size=10.1,leading=15)
    book.finish()

    book.start("PHỤ LỤC B","Median, Mode và co phương sai","math-2")
    book.title("Median, Mode và biến thiên sau điền")
    book.label("1. MEDIAN VÀ TỔNG KHOẢNG CÁCH")
    book.para("Với g(a)=Σ|xᵢ-a|, tại vị trí không trùng quan sát, độ dốc bằng số điểm bên trái trừ số điểm bên phải. Ở các điểm gãy, xét đạo hàm một phía; điều kiện tối ưu tương ứng trung vị. Với mẫu chẵn, cả khoảng giữa hai quan sát giữa đều tối ưu.")
    book.box("P(X≤m)≥1/2 và P(X≥m)≥1/2.<br/>"
             "Nếu E|X| hữu hạn và phân phối liên tục thích hợp:<br/>"
             "d E|X-a| / da = 2F(a)-1.",size=11.4,leading=18)
    book.label("2. MODE VÀ MẤT MÁT 0-1")
    book.box("Σ 1(xᵢ≠a) = n-Count(a).<br/>E[1(X≠a)] = 1-P(X=a).",size=12,leading=19)
    book.para("Chọn giá trị có Count hoặc xác suất lớn nhất làm số sai hoặc xác suất sai nhỏ nhất. Các giá trị đồng cực đại cùng tối ưu. Kết luận dùng nhãn rời rạc và chi phí sai bằng nhau.")
    book.label("3. VÌ SAO MEAN IMPUTATION CO PHƯƠNG SAI?")
    book.para("Gọi n≥2 là số ô quan sát, m là số ô được điền bằng Mean của chính n ô đó. Mean và tổng bình phương độ lệch giữ nguyên; mẫu số phương sai mẫu tăng từ n-1 thành n+m-1:")
    book.box("s<super>2</super><sub>sau</sub> = s<super>2</super><sub>quan sát</sub> × (n-1)/(n+m-1).",size=12,leading=19)
    book.para("Nếu dùng Mean từ một train khác để điền test, đẳng thức trên không tự động áp dụng cho phương sai test. Khi có thêm thông tin Z, có thể xét Mean/Median/Mode có điều kiện theo Z và kiểm chứng tính đại diện trong nhóm.",size=10.5,leading=15)
    book.finish()


GLOSSARY=[
("Phân phối","Mô tả vị trí và mức phổ biến của các giá trị. Một thống kê trung tâm không mô tả hết độ phân tán, số đỉnh và đuôi."),
("Mean / Median / Mode","Trung bình cộng / trung vị / giá trị có tần suất cực đại. Lựa chọn cần gắn với kiểu biến và mục tiêu."),
("Skewness","Hệ số bất đối xứng; pandas dùng Fisher-Pearson hiệu chỉnh cỡ mẫu. Một giá trị gần 0 chưa chứng minh chuẩn hay đối xứng."),
("Outlier / IQR","Quan sát khác biệt / Q3-Q1. Quy tắc 1,5 IQR gắn cờ ứng viên, không xác nhận dữ liệu sai."),
("Robust","Tính ít bị tác động bởi một tỷ lệ nhỏ quan sát cực đoan. Không thay thế việc đánh giá theo mục tiêu cụ thể."),
("Loss / Risk","Mức phạt của một dự đoán / mức phạt kỳ vọng theo phân phối mục tiêu."),
("E / P / F","Kỳ vọng / xác suất / hàm phân phối tích lũy F(a)=P(X≤a)."),
("argmin / argmax","Tập nghiệm làm biểu thức nhỏ nhất / lớn nhất. Ký hiệu ∈ thể hiện một giá trị thuộc tập nghiệm."),
("Moment","Kỳ vọng của một lũy thừa hoặc của độ lệch. E[X²] hữu hạn là điều kiện cho phân rã rủi ro Mean trong bài."),
("Variance / SD","Phương sai / căn phương sai. SD giữ đơn vị của biến; với phương sai mẫu thường dùng mẫu số n-1."),
("MCAR / MAR / MNAR","Ba mô hình cơ chế thiếu: độc lập dữ liệu / độc lập phần thiếu khi đã điều kiện hóa phần quan sát / vẫn phụ thuộc phần thiếu."),
("Mask / Seed","Bảng đánh dấu ô che / trạng thái khởi tạo sinh số giả ngẫu nhiên. Cùng seed và cấu hình giúp tái lập."),
("Ground truth","Giá trị gốc dùng để chấm; được giữ riêng trước khi che. Không dùng để học thống kê ở test."),
("Train / Test","Phần dữ liệu học mô hình, tiền xử lý / phần giữ riêng để đánh giá khả năng áp dụng."),
("Fit / Transform","Học tham số hoặc thống kê / dùng những gì đã học để biến đổi đầu vào."),
("Feature / Target","Biến đầu vào X / đại lượng y cần dự đoán. Trong thí nghiệm mô hình, G3 chỉ là đích và luôn đầy đủ."),
("Pipeline / Leakage","Chuỗi tiền xử lý và mô hình / thông tin test tham gia quá trình học hoặc chọn cấu hình."),
("One-hot / Chuẩn hóa","Mã hóa nhãn thành các cột chỉ báo / trừ Mean và chia SD học từ train. Ridge dùng chuẩn hóa số sau điền."),
("Ridge","Hồi quy tuyến tính với phạt L2 lên hệ số. Trong project, alpha=1 được cố định trước khi chấm test."),
("Random Forest","Tập hợp cây hồi quy lấy trung bình dự đoán. Project dùng 100 cây, min_samples_leaf=3, random_state=42."),
("MAE / RMSE","Trung bình |sai số| / căn trung bình sai số². Càng thấp càng tốt; giữ đơn vị biến, RMSE phạt lỗi lớn mạnh hơn."),
("Accuracy / R²","Tỷ lệ khớp nhãn / 1-SSE/SST. R² có thể âm và không phải tỷ lệ đối tượng dự đoán đúng."),
("SD / Khoảng tin cậy","SD mô tả dao động các lần chạy; không tự trở thành khoảng tin cậy. Các split trong project chồng lấn."),
("Prediction shift","Trung bình độ lệch tuyệt đối giữa dự đoán hiện tại và mô hình đầy đủ cùng split, cùng hàng; khác sai số với G3 thật."),
("Sensitivity / Multiple imputation","Khảo sát kết luận khi đổi giả định / tạo nhiều bộ điền để phản ánh bất định dưới mô hình phù hợp."),
("Ý nghĩa thống kê","Khác biệt quan sát giữa điểm trung bình chưa tự xác lập khác biệt ổn định hay phổ quát; cần thiết kế suy luận thích hợp."),
]


def glossary_pages(book):
    for k,(start,stop) in enumerate([(0,13),(13,26)],1):
        book.start(f"PHỤ LỤC {'C' if k==1 else 'D'}",f"Thuật ngữ {k}/2",f"glossary-{k}")
        book.title("Thuật ngữ để hiểu và giải thích",f"PHẦN {k}/2")
        book.para("Tra theo khái niệm khi tập nói. Có thể giải thích bằng tiếng Việt trước rồi nhắc tên tiếng Anh.",size=10,leading=15,color=MUTED,after=17)
        for term,meaning in GLOSSARY[start:stop]:
            book.para(f"<b>{escape(term)}</b>  {escape(meaning)}",size=10.4,leading=15.2,after=13,raw=True)
        book.finish()


def qa_page(book,models):
    book.start("PHỤ LỤC E","Kết quả và phản biện","qa")
    book.title("Bảng để đối chiếu khi hỏi đáp")
    book.para("G3 giữ đầy đủ. Thiếu 15% ở sáu đầu vào của train và test. Các cấu hình có thiếu lấy trung bình 20 tổ hợp chia/che.",size=10,leading=14.6)
    def value(model,metric,method=None):
        source=models["reference"] if method is None else models["evaluation"]
        rows=[r for r in source if r["model"]==model and r["metric"]==metric]
        if method is not None:
            rows=[r for r in rows if r["method"]==method and r["missing_rate"]==.15 and r["phase"]=="Masked train, masked test" and r["subset"]=="All test"]
        assert len(rows)==1
        return f"{rows[0]['mean']:.3f}".replace(".",",")
    data=[["Mô hình","Cấu hình","MAE","RMSE","R²"]]
    for model in ["Ridge","Random Forest"]:
        for method in [None,"Mean","Median","Mode"]:
            data.append([model,"Đầy đủ" if method is None else method,*[value(model,m,method) for m in ["MAE","RMSE","R2"]]])
    style=ParagraphStyle("cell",fontName="Body",fontSize=9.4,leading=12,textColor=INK)
    data=[[Paragraph(escape(s),style) for s in row] for row in data]
    table=Table(data,colWidths=[125,105,86,88,CW-404],rowHeights=24)
    table.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,0),PALE),("GRID",(0,0),(-1,-1),.45,LINE),
        ("VALIGN",(0,0),(-1,-1),"MIDDLE"),("LEFTPADDING",(0,0),(-1,-1),7),
        ("RIGHTPADDING",(0,0),(-1,-1),6),
        ("ROWBACKGROUNDS",(0,1),(-1,-1),[colors.white,colors.HexColor("#F6F8F8")]),
    ]))
    _,height=table.wrap(CW,H)
    table.drawOn(book.canvas,L,book.y-height)
    book.y-=height+19
    for question,answer in [
        ("Mean thắng RMSE thì luôn nên dùng Mean?","Kết luận chỉ trong dataset, biến, mô hình và MCAR đã thử. Chênh nhỏ chưa được xác lập ý nghĩa thống kê."),
        ("Vì sao Median tốt ở absences nhưng chưa tốt nhất cho G3?","Một bên chấm khôi phục một đặc trưng; bên kia chấm đích của mô hình nhiều biến và đổi cách điền nhiều cột số."),
        ("G1/G2 có hợp lệ để dự đoán G3?","Có trong bối cảnh sau khi G1/G2 đã quan sát. Dự báo đầu năm cần bỏ các điểm chưa có và chạy lại."),
        ("Các điểm G3 bằng 0 có phải dữ liệu thiếu?","Chưa có bằng chứng để gán như vậy. Miền điểm là 0-20, nên giữ trong benchmark chính; phương án loại là độ nhạy."),
        ("15% ô thiếu có bằng 15% học sinh bị thiếu?","Không. Với sáu cột che độc lập, xác suất ít nhất một ô thiếu là 1-0,85^6, khoảng 62,3%."),
    ]:
        book.para(question,size=10.2,leading=14.2,bold=True,after=3)
        book.para(answer,size=10,leading=14.2,after=11)
    book.finish()


def sources_page(book):
    book.start("NGUỒN VÀ PHẠM VI","Nguồn và giới hạn","sources")
    book.title("Nguồn và phạm vi sử dụng")
    book.label("DỮ LIỆU VÀ KẾT QUẢ")
    book.para("Paulo Cortez (2014), Student Performance, UCI, CC BY 4.0. Project dùng student-por.csv, 649 dòng môn tiếng Bồ Đào Nha, 33 cột gốc. Dữ liệu gốc đầy đủ; thiếu được tạo có kiểm soát để biết ground truth.")
    book.para("Các số trong lời thoại được đối chiếu với results/evidence.json, model_evidence.json và các CSV thực nghiệm. Chấm khôi phục trên ô test bị che; chấm mô hình trên mọi dòng test bằng G3 thật. Số trung bình là trung bình metric từng lần chạy.")
    book.para("Thực nghiệm huấn luyện có 370 lần fit: 360 cấu hình có thiếu và 10 mốc đầy đủ. Hai pha test của một cấu hình dùng cùng Pipeline đã fit. Các split chồng lấn; SD mô tả dao động, không tự coi là CI.")
    book.label("TÀI LIỆU NỀN")
    sources=[
        ("UCI - Student Performance","https://doi.org/10.24432/C5TG7T"),
        ("NIST - Measures of Location","https://www.itl.nist.gov/div898/handbook/eda/section3/eda351.htm"),
        ("NIST - Skewness and Kurtosis","https://www.itl.nist.gov/div898/handbook/eda/section3/eda35b.htm"),
        ("Rubin (1976) - Inference and Missing Data","https://doi.org/10.1093/biomet/63.3.581"),
        ("scikit-learn - SimpleImputer","https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html"),
        ("scikit-learn - Data leakage","https://scikit-learn.org/stable/common_pitfalls.html#data-leakage"),
        ("scikit-learn - Ridge / RandomForestRegressor","https://scikit-learn.org/stable/supervised_learning.html"),
    ]
    for label,url in sources:
        book.para(f'<link href="{html.escape(url,quote=True)}" color="#006D69"><u>{escape(label)}</u></link>',
                  size=10.2,leading=15.2,after=9,raw=True)
    book.y-=5
    book.box("Khung môn học dựa trên phần mô tả tài liệu giảng viên trong đặc tả đi kèm. "
             "PDF gốc từ thư mục Drive chưa truy cập được trong môi trường làm việc; các chứng minh và thực nghiệm được trình bày độc lập.",
             title="Giới hạn nguồn môn học",size=9.7,leading=14.2)
    book.para("Đây là bản biên tập lời nói từ script hiện có. Tên, thứ tự 24 slide và số liệu được giữ nhất quán; lời dẫn, chuyển ý và cách giải thích được viết lại để dễ trình bày.",size=10,leading=14.5,color=MUTED)
    book.finish()


def build(destination,font_dir=None):
    register_fonts(font_dir)
    payload=json.loads((ROOT/"presentation/script_pdf_content.json").read_text(encoding="utf-8"))
    models=json.loads((ROOT/"results/model_evidence.json").read_text(encoding="utf-8"))
    assert [s["slide"] for s in payload["slides"]]==list(range(1,25))
    book=Manuscript(destination)
    cover(book,payload)
    contents(book,payload)
    for item in payload["slides"]: slide_page(book,item)
    math_pages(book)
    glossary_pages(book)
    qa_page(book,models)
    sources_page(book)
    book.save()
    diagnostics=ROOT/"tmp/pdfs"
    diagnostics.mkdir(parents=True,exist_ok=True)
    (diagnostics/"speech_layout.json").write_text(
        json.dumps({"page_count":book.page,"checks":book.page_checks,"bounds":book.bounds},
                   ensure_ascii=False,indent=2),encoding="utf-8")
    print(f"Created {book.page} pages: {destination}")


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--output",type=Path,default=ROOT/"output/pdf/ban_thuyet_trinh_day_du.pdf")
    parser.add_argument("--font-dir",type=Path)
    args=parser.parse_args()
    build(args.output.resolve(),args.font_dir)
