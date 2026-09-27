import flet as ft
import random
from datetime import datetime

# =========================================================
# 1. بيانات الحرفيين المعتمدين والموثقين
# =========================================================
INITIAL_PROS = [
    {
        "id": 101,
        "name": "المهندس أسامة العبيدي",
        "craft": "سباكة وتمديدات 🚰",
        "phone": "+964 770 123 4567",
        "country": "العراق 🇮🇶",
        "verified": True,
        "rating": "4.9 ★",
        "price": "15,000 د.ع",
        "bio": "خبير تمديدات مياه وأنظمة تدفئة مركزية وبحث عن التسريبات بأحدث الأجهزة الإلكترونية دون تكسير."
    },
    {
        "id": 102,
        "name": "الأستاذ أحمد الشمري",
        "craft": "كهرباء وتمديدات ⚡",
        "phone": "+966 50 123 4567",
        "country": "السعودية 🇸🇦",
        "verified": True,
        "rating": "4.95 ★",
        "price": "100 ر.س",
        "bio": "مهندس كهربائي متخصص في فحص القواطع الذكية وتأسيس المنازل وأنظمة السيارات الكهربائية."
    },
    {
        "id": 103,
        "name": "مركز النجم للتكييف",
        "craft": "تكييف وتبريد ❄️",
        "phone": "+962 7 9123 4567",
        "country": "الأردن 🇯🇴",
        "verified": True,
        "rating": "4.8 ★",
        "price": "15 د.أ",
        "bio": "غسيل وتنظيف مكيفات سبليت بالضغط العالي وتصليح كروت التكييف الإنفرتر المعقدة."
    }
]

# =========================================================
# 2. التطبيق الرئيسي
# =========================================================
def main(page: ft.Page):
    # إعدادات الصفحة الأساسية للتجاوب مع الكمبيوتر والتلفون
    page.title = "خدمة العالمية | Khidma Global"
    page.theme_mode = ft.ThemeMode.DARK
    page.rtl = True  # دعم اللغة العربية والاتجاه من اليمين لليسار
    page.padding = 0
    page.window_width = 450   # قياس افتراضي شبيه بالتلفون للكمبيوتر
    page.window_height = 800

    # حالات التطبيق (State)
    wallet_balance = [250.0]
    orders_list = []
    pros_data = list(INITIAL_PROS)

    # ---------------------------------------------------------
    # التنقل وإدارة الشاشات (Navigation Engine)
    # ---------------------------------------------------------
    def change_tab(e):
        index = e.control.selected_index
        if index == 0:
            show_home()
        elif index == 1:
            show_orders()
        elif index == 2:
            show_wallet()
        elif index == 3:
            show_ai()
        elif index == 4:
            show_register()
        page.update()

    # شريط التنقل السفلي الحديث المخصص للموبايل والكمبيوتر
    navigation_bar = ft.NavigationBar(
        selected_index=0,
        on_change=change_tab,
        destinations=[
            ft.NavigationDestination(icon=ft.Icons.HOME_ROUNDED, label="الرئيسية"),
            ft.NavigationDestination(icon=ft.Icons.ASSIGNMENT_ROUNDED, label="طلباتي"),
            ft.NavigationDestination(icon=ft.Icons.ACCOUNT_BALANCE_WALLET_ROUNDED, label="المحفظة"),
            ft.NavigationDestination(icon=ft.Icons.AUTO_AWESOME_ROUNDED, label="ذكاء AI"),
            ft.NavigationDestination(icon=ft.Icons.PERSON_ADD_ROUNDED, label="تسجيل حرفي"),
        ]
    )

    # حاوية المحتوى الديناميكي
    content_area = ft.Column(expand=True, scroll=ft.ScrollMode.AUTO)

    # ---------------------------------------------------------
    # 1. شاشة الرئيسية (Home View)
    # ---------------------------------------------------------
    def show_home():
        content_area.controls.clear()
        
        # هيدر البحث والتأكيد
        search_box = ft.TextField(
            hint_text="ابحث عن خدمة، حرفي، أو مدينة...",
            prefix_icon=ft.Icons.SEARCH,
            border_radius=12,
            filled=True,
        )

        banner = ft.Container(
            content=ft.Column([
                ft.Text("🛡️ نظام التوثيق والضمان العالمي", weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_300),
                ft.Text("جميع الحرفيين موثقون بالهوية الرسميّة. أموالك بأمان عبر نظام Escrow.", size=12, color=ft.Colors.WHITE70),
            ]),
            bgcolor=ft.Colors.BLUE_GREY_900,
            padding=15,
            border_radius=12,
            margin=ft.margin.only(bottom=10)
        )

        # بطاقات الحرفيين
        pros_cards = ft.Column()
        for pro in pros_data:
            card = ft.Container(
                content=ft.Column([
                    ft.Row([
                        ft.Text(pro["name"], size=16, weight=ft.FontWeight.BOLD),
                        ft.Container(
                            content=ft.Text("معتمد ✔️", size=10, color=ft.Colors.GREEN_400),
                            bgcolor=ft.Colors.GREEN_900,
                            padding=ft.padding.all(4),
                            border_radius=6
                        ) if pro["verified"] else ft.Container()
                    ], alignment=ft.MainAxisAlignment.BETWEEN),
                    
                    ft.Text(f"{pro['craft']} • {pro['country']}", color=ft.Colors.BLUE_200, size=12),
                    ft.Text(pro["bio"], size=11, color=ft.Colors.WHITE60, max_lines=2),
                    
                    ft.Row([
                        ft.Text(f"التقييم: {pro['rating']}", size=11, color=ft.Colors.AMBER_400),
                        ft.Text(f"أجرة المعاينة: {pro['price']}", size=11, color=ft.Colors.WHITE),
                    ], alignment=ft.MainAxisAlignment.BETWEEN),
                    
                    ft.Row([
                        ft.ElevatedButton(
                            "حجز موعد 📅", 
                            style=ft.ButtonStyle(color=ft.Colors.WHITE, bgcolor=ft.Colors.GREEN_700),
                            on_click=lambda _, p=pro: open_booking_dialog(p)
                        ),
                        ft.OutlinedButton(
                            "اتصال 📞", 
                            on_click=lambda _, ph=pro['phone']: page.open(ft.SnackBar(ft.Text(f"جاري الاتصال بـ: {ph}")))
                        )
                    ], alignment=ft.MainAxisAlignment.END)
                ]),
                bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
                padding=15,
                border_radius=14,
                margin=ft.margin.only(bottom=10)
            )
            pros_cards.controls.append(card)

        content_area.controls.extend([
            ft.Container(padding=12, content=ft.Column([search_box, banner, pros_cards]))
        ])
        page.update()

    # ---------------------------------------------------------
    # 2. نافذة حجز الخدمة (Booking Dialog)
    # ---------------------------------------------------------
    def open_booking_dialog(pro):
        date_input = ft.TextField(label="التاريخ ووقت الزيارة", hint_text="مثال: غداً الساعة 4 مساءً")
        desc_input = ft.TextField(label="وصف المشكلة / العطل", multiline=True)

        def confirm_booking(e):
            if not date_input.value or not desc_input.value:
                page.open(ft.SnackBar(ft.Text("يرجى إكمال جميع الحقول المطلوب!")))
                return
            
            if wallet_balance[0] < 30.0:
                page.open(ft.SnackBar(ft.Text("رصيدك غير كافٍ! يرجى شحن المحفظة أولاً.")))
                return

            wallet_balance[0] -= 30.0
            orders_list.append({
                "id": random.randint(1000, 9999),
                "pro": pro["name"],
                "craft": pro["craft"],
                "date": date_input.value,
                "desc": desc_input.value,
                "amount": 30.0,
                "status": "قيد الانتظار ⏳"
            })
            
            dialog.open = False
            page.open(ft.SnackBar(ft.Text("تم حجز الموعد وتجميد مبلغ الضمان ($30) بنجاح!")))
            show_orders()

        dialog = ft.AlertDialog(
            title=ft.Text(f"حجز خدمة: {pro['name']}"),
            content=ft.Column([
                date_input,
                desc_input,
                ft.Text("سيتم احتجاز $30.00 كعربون معاينة في نظام الضمان الآمن.", size=11, color=ft.Colors.AMBER_300)
            ], tight=True),
            actions=[
                ft.TextButton("إلغاء", on_click=lambda _: setattr(dialog, 'open', False) or page.update()),
                ft.ElevatedButton("تاكيد ودفع الضمان 🔒", on_click=confirm_booking)
            ]
        )
        page.open(dialog)

    # ---------------------------------------------------------
    # 3. شاشة طلباتي (Orders View)
    # ---------------------------------------------------------
    def show_orders():
        content_area.controls.clear()
        
        orders_col = ft.Column()
        if not orders_list:
            orders_col.controls.append(
                ft.Container(
                    content=ft.Text("لا توجد طلبات نشطة حالياً.", color=ft.Colors.WHITE50),
                    alignment=ft.alignment.center,
                    padding=40
                )
            )
        else:
            for item in reversed(orders_list):
                orders_col.controls.append(
                    ft.Container(
                        content=ft.Column([
                            ft.Text(f"طلب #{item['id']} - {item['craft']}", weight=ft.FontWeight.BOLD),
                            ft.Text(f"الحرفي: {item['pro']} | الموعد: {item['date']}", size=12),
                            ft.Text(f"التفاصيل: {item['desc']}", size=11, color=ft.Colors.WHITE60),
                            ft.Divider(),
                            ft.Row([
                                ft.Text(f"الحالة: {item['status']}", color=ft.Colors.AMBER_400, weight=ft.FontWeight.BOLD),
                                ft.Text(f"المبلغ المحتجز: ${item['amount']}", color=ft.Colors.GREEN_400)
                            ], alignment=ft.MainAxisAlignment.BETWEEN)
                        ]),
                        bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
                        padding=15,
                        border_radius=12,
                        margin=ft.margin.only(bottom=10)
                    )
                )

        content_area.controls.append(
            ft.Container(
                padding=15,
                content=ft.Column([
                    ft.Text("📋 متابعة طلباتي وحالة العمل", size=18, weight=ft.FontWeight.BOLD),
                    orders_col
                ])
            )
        )
        page.update()

    # ---------------------------------------------------------
    # 4. شاشة المحفظة (Wallet View)
    # ---------------------------------------------------------
    def show_wallet():
        content_area.controls.clear()

        wallet_card = ft.Container(
            content=ft.Column([
                ft.Text("رصيد المحفظة المتاح", color=ft.Colors.WHITE70),
                ft.Text(f"${wallet_balance[0]:.2f} USD", size=32, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_300),
                ft.Text("🔒 جميع الأموال محمية بنظام الضمان الاجتماعي والمالي.", size=11, color=ft.Colors.WHITE50)
            ]),
            bgcolor=ft.Colors.BLUE_900,
            padding=20,
            border_radius=16,
            margin=ft.margin.only(bottom=20)
        )

        amount_field = ft.TextField(label="المبلغ المراد شحنه ($)", keyboard_type=ft.KeyboardType.NUMBER)
        
        def process_topup(e):
            try:
                amt = float(amount_field.value)
                if amt <= 0: raise ValueError
                wallet_balance[0] += amt
                amount_field.value = ""
                page.open(ft.SnackBar(ft.Text(f"تمت إضافة ${amt:.2f} بنجاح إلى محفظتك!")))
                show_wallet()
            except ValueError:
                page.open(ft.SnackBar(ft.Text("يرجى إدخال مبلغ مالي صحيح!")))

        content_area.controls.append(
            ft.Container(
                padding=15,
                content=ft.Column([
                    ft.Text("💳 محفظة خدمة الرقمية", size=18, weight=ft.FontWeight.BOLD),
                    wallet_card,
                    amount_field,
                    ft.ElevatedButton("شحن الرصيد الآن ➕", on_click=process_topup, width=400)
                ])
            )
        )
        page.update()

    # ---------------------------------------------------------
    # 5. شاشة ذكاء AI (AI Assistant)
    # ---------------------------------------------------------
    def show_ai():
        content_area.controls.clear()
        
        query_input = ft.TextField(label="صف المشكلة البرمجية أو العطل الفني...", multiline=True)
        result_box = ft.Text("", color=ft.Colors.GREEN_200, size=12)

        def run_ai(e):
            if not query_input.value: return
            result_box.value = (
                f"🤖 **تحليل الذكاء الاصطناعي للمشكلة:** '{query_input.value}'\n\n"
                "• **نوع العطل التقديري:** صيانة طارئة / تمديدات\n"
                "• **التكلفة التقديرية للقطع والعمل:** $20 - $45\n"
                "• **الحرفي المرشح الأكثر تطابقاً:** المهندس أسامة العبيدي (نسبة التطابق 97%)"
            )
            page.update()

        content_area.controls.append(
            ft.Container(
                padding=15,
                content=ft.Column([
                    ft.Text("🤖 المساعد التشخيصي الذكي", size=18, weight=ft.FontWeight.BOLD),
                    ft.Text("اكتب شرحاً بسيطاً للمشكلة وسيقوم النظام بتشخيصها واقتراح السعر والحرفي المناسب.", size=11, color=ft.Colors.WHITE60),
                    query_input,
                    ft.ElevatedButton("تشخيص العطل 🔍", on_click=run_ai, width=400),
                    ft.Divider(),
                    result_box
                ])
            )
        )
        page.update()

    # ---------------------------------------------------------
    # 6. شاشة تسجيل الحرفيين (Register View)
    # ---------------------------------------------------------
    def show_register():
        content_area.controls.clear()

        name_e = ft.TextField(label="الاسم الكامل / اسم الشركة")
        craft_e = ft.TextField(label="التخصص الرئيسي (مثال: سباكة، كهرباء)")
        phone_e = ft.TextField(label="رقم الهاتف مع رمز الدولة")
        price_e = ft.TextField(label="أجرة المعاينة الأولية")

        def submit_reg(e):
            if not name_e.value or not craft_e.value or not phone_e.value:
                page.open(ft.SnackBar(ft.Text("يرجى ملء جميع الحقول الإلزامية!")))
                return

            pros_data.append({
                "id": random.randint(200, 999),
                "name": name_e.value,
                "craft": craft_e.value,
                "phone": phone_e.value,
                "country": "الموقع الحالي 📍",
                "verified": False,
                "rating": "جديد 🆕",
                "price": price_e.value if price_e.value else "حسب الاتفاق",
                "bio": "حرفي مسجل جديد قيد التدقيق والتوثيق."
            })
            page.open(ft.SnackBar(ft.Text("تم تقديم طلبك بنجاح! سيتم مراجعة الوثائق وتفعيل حسابك.")))
            show_home()

        content_area.controls.append(
            ft.Container(
                padding=15,
                content=ft.Column([
                    ft.Text("🆔 الانضمام كـ حرفي معتمد", size=18, weight=ft.FontWeight.BOLD),
                    name_e, craft_e, phone_e, price_e,
                    ft.ElevatedButton("ارسال طلب التوثيق العالمي 🚀", on_click=submit_reg, width=400)
                ])
            )
        )
        page.update()

    # بناء هيكل الصفحة الرئيسي
    page.add(
        ft.Column([
            ft.AppBar(
                title=ft.Text("خدمة العالمية | Khidma Global", weight=ft.FontWeight.BOLD, size=16),
                bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHER,
                center_title=True
            ),
            content_area,
            navigation_bar
        ], expand=True)
    )

    # تشغيل الصفحة الرئيسية عند البداية
    show_home()

# تشغيل التطبيق
if __name__ == "__main__":
    ft.app(target=main)