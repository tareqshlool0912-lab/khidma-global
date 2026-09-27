import customtkinter as ctk
from tkinter import messagebox, filedialog
import os
import random
from datetime import datetime

# =========================================================
# 1. إعدادات المظهر والنسق البصري العالمي (Enterprise Dark UI)
# =========================================================
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

COLOR_BG = "#0B0F17"         # خلفية التطبيق الأساسية
COLOR_CARD = "#151C2C"       # ألوان الكروت والبطاقات
COLOR_CARD_HOVER = "#1E293B" # لون التمرير فوق البطاقات
COLOR_ACCENT = "#10B981"     # أخضر الاعتماد والتوثيق (Emerald)
COLOR_PRIMARY = "#2563EB"    # أزرق الهوية المؤسسية (Royal Blue)
COLOR_WARNING = "#F59E0B"    # أصفر الملاحظات والتنبيهات
COLOR_DANGER = "#EF4444"     # أحمر الإلغاء والأخطاء
COLOR_TEXT_MAIN = "#F8FAFC"  # لون النصوص الرئيسية
COLOR_TEXT_MUTED = "#94A3B8" # لون النصوص الفرعية

# =========================================================
# 2. قاموس اللغات الشامل والدعم الديناميكي لـ RTL / LTR
# =========================================================
TRANSLATIONS = {
    "ar": {
        "app_name": "خدمة العالمية | Khidma Global",
        "search_hint": "ابحث عن خدمة، حرفي، أو مدينة (مثال: سباك، برلين، بغداد)...",
        "switch_lang": "English 🌐",
        "categories": "الأقسام المتاحة في هذا السيرفر",
        "nav_home": "الرئيسية 🏠",
        "nav_orders": "طلباتي 📋",
        "nav_chat": "المحادثات 💬",
        "nav_wallet": "المحفظة 💳",
        "nav_ai": "مساعد AI 🤖",
        "nav_register": "تسجيل حرفي 🆔",
        "verified": "حرفي معتمد وموثوق ✔️",
        "unverified": "قيد التدقيق والتوثيق ⏳",
        "portfolio_title": "معرض الأعمال الموثقة (قبل وبعد):",
        "reviews_title": "تقييمات وآراء العملاء الموثقة:",
        "register_title": "التسجيل كـ حرفي معتمد في الشبكة العالمية",
        "req_id_card": "رفع صور الهوية / جواز السفر (إجباري للتوثيق):",
        "req_cert": "رفع شهادة مزاولة المهنة / السجل التجاري (اختياري):",
        "req_phone": "رقم الهاتف الدولي مع رمز الدولة (إجباري):",
        "req_name": "الاسم الكامل / اسم الشركة الخدمية:",
        "req_craft": "التخصص والمهنة الرئيسية:",
        "req_price": "أجرة المعاينة / السعر الابتدائي الأساسي:",
        "req_coverage": "نطاق التغطية الجغرافية (بالكيلومتر):",
        "upload_btn": "رفع وثائق التوثيق 📄",
        "submit_reg": "تقديم طلب الانضمام والتوثيق العالمي",
        "ai_title": "🤖 نظام الذكاء الاصطناعي التشخيصي للخدمات",
        "ai_desc": "اشرح الأعطال بأي لغة (عربي، إنجليزي، ألماني...) وسيقوم النظام بتحليل العطل، اقتراح التكلفة التقديرية، وتحديد الحرفي المعتمد في منطقتك!",
        "send": "إرسال",
        "chat_placeholder": "اكتب رسالتك للحرفي مباشرة...",
        "book_service": "حجز الموعد والدفع الآمن 📅",
        "wallet_balance": "الرصيد المتاح في المحفظة:",
        "add_funds": "شحن الرصيد ➕",
        "escrow_note": "🔒 جميع المعاملات المالية محمية بواسطة نظام الحماية الخالي من المخاطر (Escrow System). لا يتم تحرير الرصيد للحرفي إلا بعد تأكيد إتمام العمل.",
        "status_pending": "قيد الانتظار ⏳",
        "status_accepted": "تم قبول الطلب 🤝",
        "status_in_progress": "الحرفي في الطريق / جاري التنفيذ 🛠️",
        "status_completed": "مكتمل ومدفوع بنجاح ✔️"
    },
    "en": {
        "app_name": "Khidma | Global Platform",
        "search_hint": "Search service, handyman, or city (e.g. Plumber, Berlin, Baghdad)...",
        "switch_lang": "عربي 🌐",
        "categories": "Categories in Selected Server",
        "nav_home": "Home 🏠",
        "nav_orders": "Orders 📋",
        "nav_chat": "Chats 💬",
        "nav_wallet": "Wallet 💳",
        "nav_ai": "AI Assistant 🤖",
        "nav_register": "Join as Pro 🆔",
        "verified": "Verified Professional ✔️",
        "unverified": "Verification Pending ⏳",
        "portfolio_title": "Verified Work Portfolio (Before & After):",
        "reviews_title": "Verified Client Reviews:",
        "register_title": "Global Handyman KYC Registration",
        "req_id_card": "Upload Official ID / Passport (Mandatory):",
        "req_cert": "Upload Trade License / Certificate (Optional):",
        "req_phone": "International Phone Number (Mandatory):",
        "req_name": "Full Name / Company Name:",
        "req_craft": "Primary Profession / Specialty:",
        "req_price": "Base Call-out Inspection Rate:",
        "req_coverage": "Service Coverage Radius (in KM):",
        "upload_btn": "Upload Identity Document 📄",
        "submit_reg": "Submit Verification Application",
        "ai_title": "🤖 Global AI Diagnostic Matrix",
        "ai_desc": "Describe home issues in any language and the AI will analyze the fault, estimate costs, and recommend verified local pros!",
        "send": "Send",
        "chat_placeholder": "Type your message directly to the pro...",
        "book_service": "Book & Hold Funds 📅",
        "wallet_balance": "Available Wallet Balance:",
        "add_funds": "Add Funds ➕",
        "escrow_note": "🔒 All transactions are secured with Khidma Escrow. Funds are only released after you approve the completed job.",
        "status_pending": "Pending Acceptance ⏳",
        "status_accepted": "Order Accepted 🤝",
        "status_in_progress": "Pro On The Way / In Progress 🛠️",
        "status_completed": "Completed & Released ✔️"
    }
}

SERVERS = [
    "العراق / Iraq 🇮🇶",
    "الأردن / Jordan 🇯🇴",
    "السعودية / KSA 🇸🇦",
    "مصر / Egypt 🇪🇬",
    "الإمارات / UAE 🇦🇪",
    "قطر / Qatar 🇶🇦",
    "الكويت / Kuwait 🇰🇼",
    "United States 🇺🇸",
    "United Kingdom 🇬🇧",
    "Germany / ألمانيا 🇩🇪",
    "France / فرنسا 🇫🇷",
    "Canada / كندا 🇨🇦",
    "Australia / أستراليا 🇦🇺",
    "Worldwide / سيرفر عالمي 🌐"
]

# =========================================================
# 3. قاعدة البيانات العالمية الأولية (Global Database Engine)
# =========================================================
INITIAL_GLOBAL_PROS = [
    {
        "id": 101,
        "name": "المهندس أسامة العبيدي",
        "craft": "سباكة وتمديدات 🚰",
        "phone": "+964 770 123 4567",
        "country": "العراق / Iraq 🇮🇶",
        "verified": True,
        "rating": 4.9,
        "reviews_count": 128,
        "starting_price": "15,000 IQD / $10",
        "coverage": "25 KM",
        "bio": "خبير تمديدات مياه وأنظمة تدفئة مركزية وبحث عن التسريبات بأحدث الأجهزة الإلكترونية دون تكسير.",
        "portfolio": ["تركيب مضخة ذكية (بعد)", "إصلاح تسريب جداري مخفي (قبل وبعد)", "تحديث شبكة مياه مجمعات"],
        "reviews": [
            {"user": "أحمد علي", "stars": 5, "comment": "ما شاء الله شغل نظيف جداً ودقيق بالمواعيد."},
            {"user": "مصطفى جاسم", "stars": 5, "comment": "كشف التسريب بأسرع وقت وبدون أي تكسير زائد."}
        ]
    },
    {
        "id": 102,
        "name": "John Smith (Master Electrician)",
        "craft": "Electrical & Smart Home ⚡",
        "phone": "+1 (555) 019-2834",
        "country": "United States 🇺🇸",
        "verified": True,
        "rating": 4.96,
        "reviews_count": 210,
        "starting_price": "$50 USD",
        "coverage": "40 Miles",
        "bio": "Licensed master electrician. Specializing in EV charger installation, electrical panel upgrades, and smart home systems.",
        "portfolio": ["Tesla Wall Connector Setup (After)", "Main Breaker Box Overhaul", "Smart Villa Lighting Automation"],
        "reviews": [
            {"user": "Michael R.", "stars": 5, "comment": "Super professional, ultra clean work, and arrived right on schedule!"},
            {"user": "Sarah Jenkins", "stars": 5, "comment": "Upgraded our entire home panel in one afternoon."}
        ]
    },
    {
        "id": 103,
        "name": "Hans Schneider (HVAC Master)",
        "craft": "Heating & AC ❄️",
        "phone": "+49 30 1234567",
        "country": "Germany / ألمانيا 🇩🇪",
        "verified": True,
        "rating": 4.88,
        "reviews_count": 95,
        "starting_price": "45 EUR",
        "coverage": "30 KM",
        "bio": "Zertifizierter HVAC-Techniker für Wärmepumpen, Wartung und moderne Klimaanlagen.",
        "portfolio": ["Heat Pump Installation", "Commercial AC Maintenance", "Duct Repair"],
        "reviews": [
            {"user": "Lukas M.", "stars": 5, "comment": "Sehr gute Arbeit, pünktlich und hochprofessionell."},
            {"user": "Clara B.", "stars": 4, "comment": "Schneller Service und sehr sauber hinterlassen."}
        ]
    },
    {
        "id": 104,
        "name": "مركز النجم المتخصص للتكييف",
        "craft": "تكييف وتبريد ❄️",
        "phone": "+962 7 9123 4567",
        "country": "الأردن / Jordan 🇯🇴",
        "verified": True,
        "rating": 4.92,
        "reviews_count": 145,
        "starting_price": "15 JOD / $20",
        "coverage": "20 KM",
        "bio": "غسيل وتنظيف مكيفات سبليت بالضغط العالي وتصليح كروت التكييف الإنفرتر المعقدة.",
        "portfolio": ["غسيل وحدات خارجية بالضغط العالي", "صيانة كارت انفرتر متضرر"],
        "reviews": [
            {"user": "عمر الزعبي", "stars": 5, "comment": "المكيف رجع يبرد ثلج والخدمة ممتازة."}
        ]
    },
    {
        "id": 105,
        "name": "Pierre Dubois (Décor & Peinture)",
        "craft": "Painting & Decor 🎨",
        "phone": "+33 1 42 68 55 00",
        "country": "France / فرنسا 🇫🇷",
        "verified": True,
        "rating": 4.90,
        "reviews_count": 82,
        "starting_price": "40 EUR",
        "coverage": "15 KM",
        "bio": "Expert en peinture d'intérieur, effets décoratifs et rénovation d'appartements de luxe.",
        "portfolio": ["Luxury Apartment Wall Finish", "Exterior Villa Coating"],
        "reviews": [
            {"user": "Camille L.", "stars": 5, "comment": "Travail très soigné et respect des délais."}
        ]
    }
]

# =========================================================
# 4. كلاس التطبيق الرئيسي (KhidmaGlobalAdvancedApp)
# =========================================================
class KhidmaGlobalAdvancedApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.lang = "ar"
        self.selected_country = SERVERS[0]
        self.pros_list = list(INITIAL_GLOBAL_PROS)
        self.active_chat_pro = None
        self.uploaded_id_path = ""
        self.uploaded_cert_path = ""

        self.user_wallet_balance = 250.0  
        self.user_orders = []              
        self.chat_messages = {}            

        self.title("Khidma Global | منصة الخدمات وتوثيق الحرفيين العالمية")
        self.geometry("580x880")
        self.configure(fg_color=COLOR_BG)

        self.setup_ui()

    def t(self, key):
        return TRANSLATIONS[self.lang].get(key, key)

    def is_rtl(self):
        return self.lang == "ar"

    def setup_ui(self):
        for widget in self.winfo_children():
            widget.destroy()

        align_side = "right" if self.is_rtl() else "left"
        opp_side = "left" if self.is_rtl() else "right"

        # الهيدر العلوي
        top_bar = ctk.CTkFrame(self, fg_color=COLOR_CARD, corner_radius=0, height=65)
        top_bar.pack(fill="x", side="top")

        title_lbl = ctk.CTkLabel(
            top_bar, 
            text=self.t("app_name"), 
            font=("Segoe UI", 15, "bold"), 
            text_color=COLOR_ACCENT
        )
        title_lbl.pack(side=align_side, padx=12, pady=10)

        lang_btn = ctk.CTkButton(
            top_bar, 
            text=self.t("switch_lang"), 
            width=80, 
            height=32,
            fg_color="#334155", 
            hover_color="#475569",
            command=self.toggle_language
        )
        lang_btn.pack(side=opp_side, padx=6)

        self.country_spinner = ctk.CTkOptionMenu(
            top_bar, 
            values=SERVERS, 
            width=150, 
            height=32,
            fg_color="#1E293B",
            button_color=COLOR_PRIMARY,
            command=self.change_country
        )
        self.country_spinner.set(self.selected_country)
        self.country_spinner.pack(side=opp_side, padx=4)

        # حاوية المحتوى الرئيسي
        self.main_content = ctk.CTkFrame(self, fg_color="transparent")
        self.main_content.pack(fill="both", expand=True, padx=12, pady=8)

        # شريط التنقل السفلي
        bottom_nav = ctk.CTkFrame(self, height=65, fg_color=COLOR_CARD, corner_radius=0)
        bottom_nav.pack(fill="x", side="bottom")

        nav_items = [
            (self.t("nav_home"), self.show_home_page),
            (self.t("nav_orders"), self.show_orders_page),
            (self.t("nav_chat"), self.show_chat_list_page),
            (self.t("nav_wallet"), self.show_wallet_page),
            (self.t("nav_ai"), self.show_ai_page),
            (self.t("nav_register"), self.show_register_page),
        ]

        for text, command in nav_items:
            btn = ctk.CTkButton(
                bottom_nav, 
                text=text, 
                font=("Segoe UI", 10, "bold"),
                fg_color="transparent", 
                hover_color=COLOR_CARD_HOVER, 
                text_color=COLOR_TEXT_MAIN,
                command=command
            )
            btn.pack(side=align_side, expand=True, fill="both")

        self.show_home_page()

    def clear_content(self):
        for widget in self.main_content.winfo_children():
            widget.destroy()

    def show_home_page(self):
        self.clear_content()
        anchor_align = "e" if self.is_rtl() else "w"
        txt_justify = "right" if self.is_rtl() else "left"

        search_frame = ctk.CTkFrame(self.main_content, fg_color="transparent")
        search_frame.pack(fill="x", pady=(0, 6))

        search_entry = ctk.CTkEntry(
            search_frame, 
            placeholder_text=self.t("search_hint"), 
            height=40,
            font=("Segoe UI", 11),
            fg_color=COLOR_CARD,
            border_color="#334155",
            justify=txt_justify
        )
        search_entry.pack(fill="x")

        banner = ctk.CTkFrame(self.main_content, fg_color="#1E3A8A", corner_radius=12)
        banner.pack(fill="x", pady=6, ipadx=8, ipady=8)

        ctk.CTkLabel(
            banner, 
            text="🛡️ Official Global Verification System", 
            font=("Segoe UI", 12, "bold"), 
            text_color="#93C5FD"
        ).pack(anchor=anchor_align, padx=10)

        ctk.CTkLabel(
            banner, 
            text="All handymen in this network are background-checked & ID verified.", 
            font=("Segoe UI", 10), 
            text_color="#DBEAFE"
        ).pack(anchor=anchor_align, padx=10)

        ctk.CTkLabel(
            self.main_content, 
            text=self.t("categories"), 
            font=("Segoe UI", 12, "bold"), 
            text_color=COLOR_TEXT_MAIN
        ).pack(anchor=anchor_align, pady=(6, 4))

        cats_grid = ctk.CTkFrame(self.main_content, fg_color="transparent")
        cats_grid.pack(fill="x", pady=2)

        categories = [
            "Plumbing 🚰", "Electrical ⚡", "HVAC / AC ❄️",
            "Carpentry 🪵", "Painting 🎨", "Cleaning 🚚"
        ] if not self.is_rtl() else [
            "سباكة ومواسر 🚰", "كهرباء وتمديدات ⚡", "تكييف وتبريد ❄️",
            "نجارة وديكور 🪵", "دهان وتشطيبات 🎨", "نقل ونظافة 🚚"
        ]

        row, col = 0, 0
        for cat in categories:
            btn = ctk.CTkButton(
                cats_grid, 
                text=cat, 
                font=("Segoe UI", 10),
                fg_color=COLOR_CARD, 
                hover_color=COLOR_CARD_HOVER, 
                height=36,
                command=lambda c=cat: self.filter_pros_by_cat(c)
            )
            btn.grid(row=row, column=col, padx=2, pady=2, sticky="nsew")
            cats_grid.columnconfigure(col, weight=1)
            col += 1
            if col > 2:
                col = 0
                row += 1

        ctk.CTkLabel(
            self.main_content, 
            text=f"Verified Handymen in ({self.selected_country}):", 
            font=("Segoe UI", 12, "bold"),
            text_color=COLOR_TEXT_MAIN
        ).pack(anchor=anchor_align, pady=(8, 4))

        scroll_pros = ctk.CTkScrollableFrame(self.main_content, fg_color="transparent")
        scroll_pros.pack(fill="both", expand=True)

        self.render_pros_cards(scroll_pros)

    def render_pros_cards(self, parent, category_filter=None):
        align_side = "right" if self.is_rtl() else "left"
        anchor_align = "e" if self.is_rtl() else "w"

        filtered = [
            p for p in self.pros_list 
            if p["country"] == self.selected_country or self.selected_country.startswith("Worldwide") or self.selected_country.startswith("سيرفر عالمي")
        ]

        if category_filter:
            filtered = [p for p in filtered if category_filter.lower() in p["craft"].lower()]

        if not filtered:
            ctk.CTkLabel(
                parent, 
                text="No registered professionals in this server yet.\nBe the first handyman to join and get verified!", 
                font=("Segoe UI", 11), 
                text_color=COLOR_TEXT_MUTED
            ).pack(pady=30)
            return

        for pro in filtered:
            card = ctk.CTkFrame(parent, fg_color=COLOR_CARD, corner_radius=12)
            card.pack(fill="x", pady=6, padx=2)

            header_frame = ctk.CTkFrame(card, fg_color="transparent")
            header_frame.pack(fill="x", padx=12, pady=(10, 2))

            ctk.CTkLabel(
                header_frame, 
                text=pro["name"], 
                font=("Segoe UI", 13, "bold"), 
                text_color=COLOR_TEXT_MAIN
            ).pack(side=align_side)

            if pro["verified"]:
                ctk.CTkLabel(
                    header_frame, 
                    text=" ✔️ Verified Pro ", 
                    font=("Segoe UI", 9, "bold"), 
                    text_color=COLOR_ACCENT,
                    fg_color="#064E3B",
                    corner_radius=6
                ).pack(side=align_side, padx=8)

            ctk.CTkLabel(
                card, 
                text=f"{pro['craft']}  |  ★ {pro['rating']} ({pro['reviews_count']} reviews)", 
                font=("Segoe UI", 10), 
                text_color=COLOR_WARNING
            ).pack(anchor=anchor_align, padx=12)

            ctk.CTkLabel(
                card, 
                text=f"📞 Phone: {pro['phone']}   | 📍 Range: {pro.get('coverage', '20 KM')}", 
                font=("Segoe UI", 10, "bold"), 
                text_color="#60A5FA"
            ).pack(anchor=anchor_align, padx=12, pady=2)

            ctk.CTkLabel(
                card, 
                text=f"💰 Base Call-out Rate: {pro['starting_price']}", 
                font=("Segoe UI", 10), 
                text_color=COLOR_TEXT_MUTED
            ).pack(anchor=anchor_align, padx=12)

            action_frame = ctk.CTkFrame(card, fg_color="transparent")
            action_frame.pack(fill="x", padx=12, pady=10)

            ctk.CTkButton(
                action_frame, 
                text="Profile 📂", 
                font=("Segoe UI", 10, "bold"),
                fg_color=COLOR_PRIMARY,
                height=30,
                command=lambda p=pro: self.show_pro_details(p)
            ).pack(side=align_side, expand=True, fill="x", padx=2)

            ctk.CTkButton(
                action_frame, 
                text="Chat 💬", 
                font=("Segoe UI", 10, "bold"),
                fg_color="#059669",
                hover_color="#047857",
                height=30,
                command=lambda p=pro: self.open_chat_with_pro(p)
            ).pack(side=align_side, expand=True, fill="x", padx=2)

            ctk.CTkButton(
                action_frame, 
                text="Book Job 📅", 
                font=("Segoe UI", 10, "bold"),
                fg_color="#7C3AED",
                hover_color="#6D28D9",
                height=30,
                command=lambda p=pro: self.open_booking_dialog(p)
            ).pack(side=align_side, expand=True, fill="x", padx=2)

    def filter_pros_by_cat(self, category):
        self.clear_content()
        anchor_align = "e" if self.is_rtl() else "w"

        ctk.CTkLabel(
            self.main_content, 
            text=f"Category Filter: {category}", 
            font=("Segoe UI", 13, "bold"), 
            text_color=COLOR_ACCENT
        ).pack(anchor=anchor_align, pady=8)

        ctk.CTkButton(
            self.main_content, 
            text="← Back to Home", 
            width=110, 
            fg_color="#334155", 
            command=self.show_home_page
        ).pack(anchor=anchor_align, pady=4)

        scroll_pros = ctk.CTkScrollableFrame(self.main_content, fg_color="transparent")
        scroll_pros.pack(fill="both", expand=True, pady=6)

        self.render_pros_cards(scroll_pros, category_filter=category.split()[0])

    def show_pro_details(self, pro):
        self.clear_content()
        anchor_align = "e" if self.is_rtl() else "w"

        scroll = ctk.CTkScrollableFrame(self.main_content, fg_color="transparent")
        scroll.pack(fill="both", expand=True)

        ctk.CTkButton(
            scroll, 
            text="← Back to List", 
            width=100, 
            fg_color="#334155", 
            command=self.show_home_page
        ).pack(anchor=anchor_align, pady=4)

        profile_card = ctk.CTkFrame(scroll, fg_color=COLOR_CARD, corner_radius=12)
        profile_card.pack(fill="x", pady=6)

        ctk.CTkLabel(profile_card, text=pro["name"], font=("Segoe UI", 15, "bold"), text_color=COLOR_TEXT_MAIN).pack(pady=(12, 2))
        ctk.CTkLabel(profile_card, text=f"Specialty: {pro['craft']}", font=("Segoe UI", 11), text_color=COLOR_ACCENT).pack(pady=2)

        info_frame = ctk.CTkFrame(profile_card, fg_color="#0F172A", corner_radius=8)
        info_frame.pack(fill="x", padx=12, pady=10)

        ctk.CTkLabel(info_frame, text=f"📞 Direct Phone: {pro['phone']}", font=("Segoe UI", 11, "bold"), text_color="#60A5FA").pack(pady=4)
        ctk.CTkLabel(info_frame, text=f"🏷️ Inspection Rate: {pro['starting_price']}", font=("Segoe UI", 10), text_color=COLOR_WARNING).pack(pady=4)
        ctk.CTkLabel(info_frame, text=f"📍 Coverage Radius: {pro.get('coverage', '25 KM')}", font=("Segoe UI", 10), text_color=COLOR_TEXT_MUTED).pack(pady=4)

        ctk.CTkLabel(scroll, text="Bio & Description:", font=("Segoe UI", 11, "bold"), text_color=COLOR_TEXT_MAIN).pack(anchor=anchor_align, pady=(10, 2))
        ctk.CTkLabel(scroll, text=pro.get("bio", "No bio provided."), font=("Segoe UI", 10), text_color=COLOR_TEXT_MUTED, wraplength=480, justify="right" if self.is_rtl() else "left").pack(anchor=anchor_align, pady=(0, 8))

        ctk.CTkLabel(scroll, text=self.t("portfolio_title"), font=("Segoe UI", 12, "bold"), text_color=COLOR_TEXT_MAIN).pack(anchor=anchor_align, pady=(12, 4))

        for sample in pro.get("portfolio", []):
            item_box = ctk.CTkFrame(scroll, fg_color=COLOR_CARD, corner_radius=8)
            item_box.pack(fill="x", pady=3)
            ctk.CTkLabel(item_box, text=f"🖼️ Verified Project: {sample}", font=("Segoe UI", 10), text_color=COLOR_TEXT_MAIN).pack(padx=10, pady=8, anchor=anchor_align)

        ctk.CTkLabel(scroll, text=self.t("reviews_title"), font=("Segoe UI", 12, "bold"), text_color=COLOR_TEXT_MAIN).pack(anchor=anchor_align, pady=(12, 4))

        for rev in pro.get("reviews", []):
            rev_box = ctk.CTkFrame(scroll, fg_color=COLOR_CARD, corner_radius=8)
            rev_box.pack(fill="x", pady=3)
            ctk.CTkLabel(rev_box, text=f"👤 {rev['user']} - {'★'*rev['stars']}", font=("Segoe UI", 10, "bold"), text_color=COLOR_WARNING).pack(anchor=anchor_align, padx=10, pady=(6, 2))
            ctk.CTkLabel(rev_box, text=f"\"{rev['comment']}\"", font=("Segoe UI", 9), text_color=COLOR_TEXT_MUTED).pack(anchor=anchor_align, padx=10, pady=(0, 6))

        btn_frame = ctk.CTkFrame(scroll, fg_color="transparent")
        btn_frame.pack(fill="x", pady=12)

        ctk.CTkButton(
            btn_frame, 
            text=f"Direct Call ({pro['phone']})", 
            font=("Segoe UI", 11, "bold"), 
            fg_color="#16A34A", 
            height=38,
            command=lambda: messagebox.showinfo("Call Pro", f"Calling {pro['name']} at:\n{pro['phone']}")
        ).pack(side="left", expand=True, fill="x", padx=2)

        ctk.CTkButton(
            btn_frame, 
            text="Book Job Now 📅", 
            font=("Segoe UI", 11, "bold"), 
            fg_color="#7C3AED", 
            height=38,
            command=lambda: self.open_booking_dialog(pro)
        ).pack(side="right", expand=True, fill="x", padx=2)

    def open_booking_dialog(self, pro):
        dialog = ctk.CTkToplevel(self)
        dialog.title(f"Book Service: {pro['name']}")
        dialog.geometry("440x520")
        dialog.configure(fg_color=COLOR_BG)
        dialog.grab_set()

        anchor_align = "e" if self.is_rtl() else "w"
        txt_justify = "right" if self.is_rtl() else "left"

        ctk.CTkLabel(dialog, text=f"Book Appointment with {pro['name']}", font=("Segoe UI", 13, "bold"), text_color=COLOR_ACCENT).pack(pady=12)

        ctk.CTkLabel(dialog, text="Select Preferred Date & Time:", font=("Segoe UI", 11)).pack(anchor=anchor_align, padx=20, pady=2)
        date_entry = ctk.CTkEntry(dialog, placeholder_text="e.g. Tomorrow at 3:00 PM", justify=txt_justify)
        date_entry.pack(fill="x", padx=20, pady=4)

        ctk.CTkLabel(dialog, text="Problem Description / Location Notes:", font=("Segoe UI", 11)).pack(anchor=anchor_align, padx=20, pady=2)
        desc_entry = ctk.CTkEntry(dialog, placeholder_text="e.g. Water leak under kitchen sink", justify=txt_justify)
        desc_entry.pack(fill="x", padx=20, pady=4)

        ctk.CTkLabel(dialog, text="Initial Call-out Holding Deposit: $30.00 USD", font=("Segoe UI", 11, "bold"), text_color=COLOR_WARNING).pack(pady=10)

        ctk.CTkLabel(dialog, text=self.t("escrow_note"), font=("Segoe UI", 9), text_color=COLOR_TEXT_MUTED, wraplength=380).pack(padx=20, pady=6)

        def confirm_booking():
            dt = date_entry.get().strip()
            desc = desc_entry.get().strip()

            if not dt or not desc:
                messagebox.showwarning("Incomplete Data", "Please fill in date and problem description!", parent=dialog)
                return

            if self.user_wallet_balance < 30.0:
                messagebox.showerror("Insufficient Balance", "Your wallet balance is insufficient! Please top up first.", parent=dialog)
                return

            self.user_wallet_balance -= 30.0
            new_order = {
                "id": random.randint(10000, 99999),
                "pro_name": pro["name"],
                "craft": pro["craft"],
                "date": dt,
                "desc": desc,
                "amount": 30.0,
                "status": self.t("status_pending"),
                "created_at": datetime.now().strftime("%Y-%m-%d %H:%M")
            }
            self.user_orders.append(new_order)

            dialog.destroy()
            messagebox.showinfo("Booking Successful", f"Order #{new_order['id']} created!\n$30.00 USD held safely in Escrow.")
            self.show_orders_page()

        ctk.CTkButton(dialog, text="Confirm & Hold Funds 🔒", font=("Segoe UI", 12, "bold"), fg_color=COLOR_ACCENT, height=40, command=confirm_booking).pack(fill="x", padx=20, pady=16)

    def show_orders_page(self):
        self.clear_content()
        anchor_align = "e" if self.is_rtl() else "w"

        ctk.CTkLabel(self.main_content, text="📋 My Service Bookings & Orders Tracker", font=("Segoe UI", 13, "bold"), text_color=COLOR_TEXT_MAIN).pack(anchor=anchor_align, pady=8)

        if not self.user_orders:
            ctk.CTkLabel(self.main_content, text="You have no active orders yet.\nBook a handyman from the home screen!", font=("Segoe UI", 11), text_color=COLOR_TEXT_MUTED).pack(pady=50)
            return

        scroll_orders = ctk.CTkScrollableFrame(self.main_content, fg_color="transparent")
        scroll_orders.pack(fill="both", expand=True)

        for order in reversed(self.user_orders):
            card = ctk.CTkFrame(scroll_orders, fg_color=COLOR_CARD, corner_radius=12)
            card.pack(fill="x", pady=6, padx=2)

            ctk.CTkLabel(card, text=f"Order #{order['id']} - {order['craft']}", font=("Segoe UI", 12, "bold"), text_color=COLOR_ACCENT).pack(anchor=anchor_align, padx=12, pady=(8, 2))
            ctk.CTkLabel(card, text=f"Pro: {order['pro_name']} | Date: {order['date']}", font=("Segoe UI", 10), text_color=COLOR_TEXT_MAIN).pack(anchor=anchor_align, padx=12)
            ctk.CTkLabel(card, text=f"Notes: {order['desc']}", font=("Segoe UI", 10), text_color=COLOR_TEXT_MUTED).pack(anchor=anchor_align, padx=12, pady=2)

            status_box = ctk.CTkFrame(card, fg_color="#0F172A", corner_radius=6)
            status_box.pack(fill="x", padx=12, pady=6)

            ctk.CTkLabel(status_box, text=f"Status: {order['status']}", font=("Segoe UI", 10, "bold"), text_color=COLOR_WARNING).pack(side="left", padx=10, pady=6)
            ctk.CTkLabel(status_box, text=f"Held Escrow Amount: ${order['amount']} USD", font=("Segoe UI", 9), text_color="#60A5FA").pack(side="right", padx=10, pady=6)

            if order["status"] == self.t("status_pending"):
                btn_accept = ctk.CTkButton(card, text="Simulate Pro Accepts 🤝", font=("Segoe UI", 10), fg_color="#334155", command=lambda o=order: self.update_order_status(o, self.t("status_in_progress")))
                btn_accept.pack(anchor="e" if self.is_rtl() else "w", padx=12, pady=(0, 8))

            elif order["status"] == self.t("status_in_progress"):
                btn_complete = ctk.CTkButton(card, text="Confirm Work Done & Release Funds ✔️", font=("Segoe UI", 10, "bold"), fg_color=COLOR_ACCENT, command=lambda o=order: self.update_order_status(o, self.t("status_completed")))
                btn_complete.pack(fill="x", padx=12, pady=(0, 8))

    def update_order_status(self, order, new_status):
        order["status"] = new_status
        messagebox.showinfo("Status Updated", f"Order #{order['id']} status changed to:\n{new_status}")
        self.show_orders_page()

    def show_wallet_page(self):
        self.clear_content()
        anchor_align = "e" if self.is_rtl() else "w"

        ctk.CTkLabel(self.main_content, text="💳 Khidma Escrow Digital Wallet", font=("Segoe UI", 13, "bold"), text_color=COLOR_TEXT_MAIN).pack(anchor=anchor_align, pady=8)

        card = ctk.CTkFrame(self.main_content, fg_color="#1E3A8A", corner_radius=14)
        card.pack(fill="x", pady=8, ipadx=10, ipady=12)

        ctk.CTkLabel(card, text=self.t("wallet_balance"), font=("Segoe UI", 11), text_color="#DBEAFE").pack(anchor=anchor_align, padx=12)
        ctk.CTkLabel(card, text=f"${self.user_wallet_balance:.2f} USD", font=("Segoe UI", 22, "bold"), text_color="#FFFFFF").pack(anchor=anchor_align, padx=12, pady=4)

        ctk.CTkLabel(self.main_content, text=self.t("escrow_note"), font=("Segoe UI", 10), text_color=COLOR_TEXT_MUTED, wraplength=480, justify="right" if self.is_rtl() else "left").pack(anchor=anchor_align, pady=8)

        ctk.CTkButton(
            self.main_content, 
            text=self.t("add_funds"), 
            font=("Segoe UI", 11, "bold"), 
            fg_color=COLOR_ACCENT, 
            height=40,
            command=self.topup_wallet_dialog
        ).pack(fill="x", pady=10)

    def topup_wallet_dialog(self):
        dialog = ctk.CTkToplevel(self)
        dialog.title("Add Funds to Wallet")
        dialog.geometry("380x300")
        dialog.configure(fg_color=COLOR_BG)
        dialog.grab_set()

        ctk.CTkLabel(dialog, text="Top Up Balance", font=("Segoe UI", 13, "bold")).pack(pady=12)

        amount_entry = ctk.CTkEntry(dialog, placeholder_text="Enter amount in USD ($)")
        amount_entry.pack(fill="x", padx=20, pady=8)

        method_spinner = ctk.CTkOptionMenu(dialog, values=["Credit / Debit Card 💳", "PayPal 🌐", "ZainCash / Local Wallet 📱", "Crypto (USDT) 🪙"])
        method_spinner.pack(fill="x", padx=20, pady=8)

        def process_topup():
            val = amount_entry.get().strip()
            if val.isdigit() or val.replace('.', '', 1).isdigit():
                add_val = float(val)
                self.user_wallet_balance += add_val
                dialog.destroy()
                messagebox.showinfo("Success", f"Successfully added ${add_val:.2f} USD to your wallet!")
                self.show_wallet_page()
            else:
                messagebox.showerror("Error", "Please enter a valid numeric amount.")

        ctk.CTkButton(dialog, text="Proceed Payment", fg_color=COLOR_PRIMARY, command=process_topup).pack(fill="x", padx=20, pady=16)

    def show_register_page(self):
        self.clear_content()
        anchor_align = "e" if self.is_rtl() else "w"
        txt_justify = "right" if self.is_rtl() else "left"

        scroll = ctk.CTkScrollableFrame(self.main_content, fg_color="transparent")
        scroll.pack(fill="both", expand=True)

        ctk.CTkLabel(scroll, text=self.t("register_title"), font=("Segoe UI", 13, "bold"), text_color=COLOR_ACCENT).pack(pady=8)

        ctk.CTkLabel(scroll, text=self.t("req_name"), font=("Segoe UI", 10)).pack(anchor=anchor_align, pady=2)
        name_entry = ctk.CTkEntry(scroll, placeholder_text="Full Name / Business Name", justify=txt_justify)
        name_entry.pack(fill="x", pady=4)

        ctk.CTkLabel(scroll, text=self.t("req_phone"), font=("Segoe UI", 10, "bold"), text_color="#60A5FA").pack(anchor=anchor_align, pady=2)
        phone_entry = ctk.CTkEntry(scroll, placeholder_text="+1 555-0192 or +964 770-0000", justify=txt_justify)
        phone_entry.pack(fill="x", pady=4)

        ctk.CTkLabel(scroll, text=self.t("req_craft"), font=("Segoe UI", 10)).pack(anchor=anchor_align, pady=2)
        craft_spinner = ctk.CTkOptionMenu(scroll, values=["Plumbing 🚰", "Electrical ⚡", "HVAC / AC ❄️", "Carpentry 🪵", "Painting 🎨", "Cleaning 🚚"])
        craft_spinner.pack(fill="x", pady=4)

        ctk.CTkLabel(scroll, text=self.t("req_price"), font=("Segoe UI", 10)).pack(anchor=anchor_align, pady=2)
        price_entry = ctk.CTkEntry(scroll, placeholder_text="e.g. $25 USD / 15,000 IQD", justify=txt_justify)
        price_entry.pack(fill="x", pady=4)

        ctk.CTkLabel(scroll, text=self.t("req_coverage"), font=("Segoe UI", 10)).pack(anchor=anchor_align, pady=2)
        cov_entry = ctk.CTkEntry(scroll, placeholder_text="e.g. 25 KM", justify=txt_justify)
        cov_entry.pack(fill="x", pady=4)

        ctk.CTkLabel(scroll, text=self.t("req_id_card"), font=("Segoe UI", 10, "bold"), text_color=COLOR_WARNING).pack(anchor=anchor_align, pady=(8, 2))
        id_status_lbl = ctk.CTkLabel(scroll, text="No ID file selected ⚠️", font=("Segoe UI", 9), text_color=COLOR_TEXT_MUTED)

        def choose_id_file():
            file_path = filedialog.askopenfilename(title="Select Passport or National ID", filetypes=[("Images & PDFs", "*.jpg *.png *.pdf")])
            if file_path:
                self.uploaded_id_path = file_path
                filename = os.path.basename(file_path)
                id_status_lbl.configure(text=f"Uploaded: {filename} ✔️", text_color=COLOR_ACCENT)

        upload_btn = ctk.CTkButton(scroll, text=self.t("upload_btn"), fg_color="#334155", command=choose_id_file)
        upload_btn.pack(fill="x", pady=4)
        id_status_lbl.pack(pady=2)

        def submit_registration():
            n = name_entry.get().strip()
            p = phone_entry.get().strip()
            pr = price_entry.get().strip()
            cov = cov_entry.get().strip() or "20 KM"

            if not n or not p or not pr:
                messagebox.showwarning("Warning", "Please fill in all required fields!")
                return
            
            if not self.uploaded_id_path:
                messagebox.showwarning("Verification Required", "ID verification is mandatory for global safety!")
                return

            new_pro = {
                "id": len(self.pros_list) + 200,
                "name": n,
                "craft": craft_spinner.get(),
                "phone": p,
                "country": self.selected_country,
                "verified": True,
                "rating": 5.0,
                "reviews_count": 1,
                "starting_price": pr,
                "coverage": cov,
                "bio": "Global verified handyman.",
                "portfolio": ["Initial Verified Work Portfolio"],
                "reviews": [{"user": "Khidma Global Verification", "stars": 5, "comment": "ID and phone credentials successfully verified."}]
            }

            self.pros_list.append(new_pro)
            messagebox.showinfo("Success", "Your profile and identity have been verified! You are now live on the selected server 🎉")
            self.show_home_page()

        ctk.CTkButton(scroll, text=self.t("submit_reg"), font=("Segoe UI", 11, "bold"), fg_color=COLOR_ACCENT, height=40, command=submit_registration).pack(fill="x", pady=16)

    def open_chat_with_pro(self, pro):
        self.active_chat_pro = pro
        self.show_chat_room_page()

    def show_chat_list_page(self):
        self.clear_content()

        ctk.CTkLabel(self.main_content, text="💬 Active Chats", font=("Segoe UI", 13, "bold"), text_color=COLOR_TEXT_MAIN).pack(anchor="e" if self.is_rtl() else "w", pady=8)

        if not self.active_chat_pro:
            ctk.CTkLabel(self.main_content, text="No active chats.\nStart a conversation with any handyman from the home screen!", font=("Segoe UI", 11), text_color=COLOR_TEXT_MUTED).pack(pady=40)
        else:
            card = ctk.CTkFrame(self.main_content, fg_color=COLOR_CARD, corner_radius=10)
            card.pack(fill="x", pady=5)
            ctk.CTkLabel(card, text=f"Chat with: {self.active_chat_pro['name']}", font=("Segoe UI", 11, "bold")).pack(anchor="e" if self.is_rtl() else "w", padx=10, pady=(8, 2))
            ctk.CTkButton(card, text="Open Room 💬", width=90, fg_color=COLOR_PRIMARY, command=self.show_chat_room_page).pack(anchor="w" if self.is_rtl() else "e", padx=10, pady=6)

    def show_chat_room_page(self):
        self.clear_content()
        pro = self.active_chat_pro
        if not pro:
            self.show_chat_list_page()
            return

        header = ctk.CTkFrame(self.main_content, fg_color=COLOR_CARD, corner_radius=8)
        header.pack(fill="x", pady=(0, 6))

        ctk.CTkLabel(header, text=f"💬 Chat Room: {pro['name']}", font=("Segoe UI", 11, "bold"), text_color=COLOR_ACCENT).pack(side="right" if self.is_rtl() else "left", padx=10, pady=8)

        chat_box = ctk.CTkTextbox(self.main_content, fg_color=COLOR_CARD, font=("Segoe UI", 11))
        chat_box.pack(fill="both", expand=True, pady=4)

        chat_box.insert("end", f"System: Encrypted end-to-end chat room opened with {pro['name']}.\n")
        chat_box.insert("end", f"Direct Phone: {pro['phone']}\n-------------------------------------------------\n")

        history = self.chat_messages.get(pro["id"], [])
        for sender, msg in history:
            chat_box.insert("end", f"\n{sender}: {msg}\n")

        entry_frame = ctk.CTkFrame(self.main_content, fg_color="transparent")
        entry_frame.pack(fill="x", pady=4)

        msg_input = ctk.CTkEntry(entry_frame, placeholder_text=self.t("chat_placeholder"), justify="right" if self.is_rtl() else "left")
        msg_input.pack(side="right" if self.is_rtl() else "left", fill="x", expand=True, padx=4)

        def send_message():
            txt = msg_input.get().strip()
            if txt:
                chat_box.insert("end", f"\nYou: {txt}\n")
                chat_box.insert("end", f"{pro['name']}: Thanks for reaching out! I will review and reply shortly.\n")

                if pro["id"] not in self.chat_messages:
                    self.chat_messages[pro["id"]] = []

                self.chat_messages[pro["id"]].append(("You", txt))
                self.chat_messages[pro["id"]].append((pro["name"], "Thanks for reaching out! I will review and reply shortly."))

                msg_input.delete(0, 'end')

        ctk.CTkButton(entry_frame, text=self.t("send"), width=70, fg_color=COLOR_PRIMARY, command=send_message).pack(side="left" if self.is_rtl() else "right")

    def show_ai_page(self):
        self.clear_content()

        ctk.CTkLabel(self.main_content, text=self.t("ai_title"), font=("Segoe UI", 13, "bold"), text_color="#60A5FA").pack(pady=4)
        ctk.CTkLabel(self.main_content, text=self.t("ai_desc"), font=("Segoe UI", 10), text_color=COLOR_TEXT_MUTED, wraplength=460, justify="right" if self.is_rtl() else "left").pack(pady=(0, 6))

        chat_box = ctk.CTkTextbox(self.main_content, fg_color=COLOR_CARD, font=("Segoe UI", 11))
        chat_box.pack(fill="both", expand=True, pady=4)

        chat_box.insert("end", f"🤖 Khidma AI Assistant: Hello! Describe any issue in your home/office in any language...\nActive Server Context: {self.selected_country}\n-------------------------------------------------\n")

        entry_frame = ctk.CTkFrame(self.main_content, fg_color="transparent")
        entry_frame.pack(fill="x", pady=4)

        ai_input = ctk.CTkEntry(entry_frame, placeholder_text="Describe fault (e.g., water leak, short circuit)...", justify="right" if self.is_rtl() else "left")
        ai_input.pack(side="right" if self.is_rtl() else "left", fill="x", expand=True, padx=4)

        def ask_ai():
            query = ai_input.get().strip()
            if query:
                chat_box.insert("end", f"\nYou: {query}\n")
                
                q_lower = query.lower()
                category_detected = "General Maintenance 🛠️"
                cost_estimate = "$20 - $50 USD"

                if "water" in q_lower or "leak" in q_lower or "مياه" in q_lower or "تسريب" in q_lower or "سباك" in q_lower:
                    category_detected = "Plumbing / السباكة 🚰"
                    cost_estimate = "$25 - $60 USD"
                elif "electric" in q_lower or "power" in q_lower or "كهرباء" in q_lower or "انقطاع" in q_lower:
                    category_detected = "Electrical / الكهرباء ⚡"
                    cost_estimate = "$30 - $75 USD"
                elif "ac" in q_lower or "heat" in q_lower or "مكيف" in q_lower or "تبريد" in q_lower or "klima" in q_lower:
                    category_detected = "HVAC & AC / التكييف ❄️"
                    cost_estimate = "$35 - $90 USD"

                reply = (
                    f"🤖 Khidma AI Diagnostic Result:\n"
                    f"• Fault Category: {category_detected}\n"
                    f"• Safety Precaution: Turn off main supply valves/switches if leaking or sparking!\n"
                    f"• Estimated Fix Cost in {self.selected_country}: {cost_estimate}\n"
                    f"• Recommended Action: Check verified professionals in your home page.\n"
                )

                chat_box.insert("end", reply + "\n")
                ai_input.delete(0, 'end')

        ctk.CTkButton(entry_frame, text="Diagnose 🔍", width=90, fg_color=COLOR_PRIMARY, command=ask_ai).pack(side="left" if self.is_rtl() else "right")

    def toggle_language(self):
        self.lang = "en" if self.lang == "ar" else "ar"
        self.setup_ui()

    def change_country(self, choice):
        self.selected_country = choice
        self.show_home_page()

if __name__ == "__main__":
    app = KhidmaGlobalAdvancedApp()
    app.mainloop()