# -*- coding: utf-8 -*-
import os
import pptx
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def build_presentation():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    assets_dir = r"C:\Users\marsr\busqueda-rutas-app\report\assets"
    logo_path = os.path.join(assets_dir, "upc_logo.png")
    graph_path = os.path.join(assets_dir, "sudoku_graph.png")
    uml_path = os.path.join(assets_dir, "uml_model.png")
    gui_board_path = os.path.join(assets_dir, "gui_main_board.png")
    gui_solved_path = os.path.join(assets_dir, "gui_solved_telemetry.png")
    gui_4x4_path = os.path.join(assets_dir, "gui_dimension_4x4.png")
    gui_16x16_path = os.path.join(assets_dir, "gui_dimension_16x16.png")

    # Colors
    C_DARK_BG = RGBColor(15, 23, 42)      # #0F172A
    C_NAVY = RGBColor(30, 58, 138)        # #1E3A8A
    C_UPC_RED = RGBColor(220, 38, 38)     # #DC2626
    C_LIGHT_BG = RGBColor(248, 250, 252)  # #F8FAFC
    C_CARD_BG = RGBColor(255, 255, 255)   # #FFFFFF
    C_BORDER = RGBColor(203, 213, 225)    # #CBD5E1
    C_TEXT_DARK = RGBColor(30, 41, 59)    # #1E293B
    C_TEXT_MUTED = RGBColor(100, 116, 139)# #64748B
    C_ACCENT_BLUE = RGBColor(37, 99, 235) # #2563EB
    C_SUCCESS = RGBColor(16, 185, 129)    # #10B981
    C_WHITE = RGBColor(255, 255, 255)

    def add_header(slide, title_text, category_text, speaker_name, slide_num):
        top_bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(1.15))
        top_bar.fill.solid()
        top_bar.fill.fore_color.rgb = C_DARK_BG
        top_bar.line.fill.background()

        stripe = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(1.15), Inches(13.333), Inches(0.06))
        stripe.fill.solid()
        stripe.fill.fore_color.rgb = C_UPC_RED
        stripe.line.fill.background()

        tb = slide.shapes.add_textbox(Inches(0.8), Inches(0.12), Inches(8.5), Inches(0.95))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        
        p0 = tf.paragraphs[0]
        p0.text = category_text.upper()
        p0.font.name = "Segoe UI"
        p0.font.size = Pt(10)
        p0.font.bold = True
        p0.font.color.rgb = C_UPC_RED
        
        p1 = tf.add_paragraph()
        p1.text = title_text
        p1.font.name = "Segoe UI"
        p1.font.size = Pt(20)
        p1.font.bold = True
        p1.font.color.rgb = C_WHITE

        badge = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(9.5), Inches(0.25), Inches(3.0), Inches(0.65))
        badge.fill.solid()
        badge.fill.fore_color.rgb = RGBColor(30, 41, 59)
        badge.line.color.rgb = RGBColor(71, 85, 105)
        badge.line.width = Pt(1)
        
        btf = badge.text_frame
        btf.margin_left = btf.margin_top = btf.margin_right = btf.margin_bottom = 0
        bp0 = btf.paragraphs[0]
        bp0.text = "PONENTE:"
        bp0.font.name = "Segoe UI"
        bp0.font.size = Pt(8.5)
        bp0.font.bold = True
        bp0.font.color.rgb = RGBColor(148, 163, 184)
        bp0.alignment = PP_ALIGN.CENTER
        
        bp1 = btf.add_paragraph()
        bp1.text = speaker_name
        bp1.font.name = "Segoe UI"
        bp1.font.size = Pt(11)
        bp1.font.bold = True
        bp1.font.color.rgb = C_WHITE
        bp1.alignment = PP_ALIGN.CENTER

        # Footer
        footer = slide.shapes.add_textbox(Inches(11.5), Inches(7.1), Inches(1.2), Inches(0.3))
        ftf = footer.text_frame
        fp = ftf.paragraphs[0]
        fp.text = f"{slide_num} / 13"
        fp.font.name = "Segoe UI"
        fp.font.size = Pt(10)
        fp.font.color.rgb = C_TEXT_MUTED
        fp.alignment = PP_ALIGN.RIGHT

        ft_line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(7.05), Inches(11.733), Inches(0.02))
        ft_line.fill.solid()
        ft_line.fill.fore_color.rgb = C_BORDER
        ft_line.line.fill.background()
        
        ft_lbl = slide.shapes.add_textbox(Inches(0.8), Inches(7.1), Inches(8.0), Inches(0.3))
        ft_lbl.text_frame.paragraphs[0].text = "UPC - Complejidad Algorítmica (1ACC0184) | Grupo 5 - Sección 4749"
        ft_lbl.text_frame.paragraphs[0].font.size = Pt(9.5)
        ft_lbl.text_frame.paragraphs[0].font.color.rgb = C_TEXT_MUTED

    def add_card(slide, left, top, width, height, title="", border_color=C_BORDER):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(left), Inches(top), Inches(width), Inches(height))
        card.fill.solid()
        card.fill.fore_color.rgb = C_CARD_BG
        card.line.color.rgb = border_color
        card.line.width = Pt(1.5)
        
        if title:
            tb = slide.shapes.add_textbox(Inches(left + 0.25), Inches(top + 0.18), Inches(width - 0.5), Inches(0.4))
            tf = tb.text_frame
            tf.word_wrap = True
            tf.margin_top = tf.margin_bottom = tf.margin_left = tf.margin_right = 0
            p = tf.paragraphs[0]
            p.text = title
            p.font.name = "Segoe UI"
            p.font.size = Pt(14)
            p.font.bold = True
            p.font.color.rgb = C_NAVY
        return card

    def add_metric_box(slide, left, top, width, height, value_text, label_text, accent_color=C_ACCENT_BLUE):
        box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(left), Inches(top), Inches(width), Inches(height))
        box.fill.solid()
        box.fill.fore_color.rgb = RGBColor(241, 245, 249)
        box.line.color.rgb = accent_color
        box.line.width = Pt(1.5)
        
        tb = slide.shapes.add_textbox(Inches(left), Inches(top + 0.1), Inches(width), Inches(height - 0.2))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
        
        p0 = tf.paragraphs[0]
        p0.text = value_text
        p0.font.name = "Segoe UI"
        p0.font.size = Pt(22)
        p0.font.bold = True
        p0.font.color.rgb = accent_color
        p0.alignment = PP_ALIGN.CENTER
        
        p1 = tf.add_paragraph()
        p1.text = label_text
        p1.font.name = "Segoe UI"
        p1.font.size = Pt(10)
        p1.font.color.rgb = C_TEXT_DARK
        p1.alignment = PP_ALIGN.CENTER

    # =========================================================================
    # SLIDE 1: PORTADA OFICIAL
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    bg1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5))
    bg1.fill.solid()
    bg1.fill.fore_color.rgb = C_DARK_BG
    bg1.line.fill.background()

    # Red accent stripe top
    s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(0.12)).fill.solid()
    s1.shapes[-1].fill.fore_color.rgb = C_UPC_RED
    s1.shapes[-1].line.fill.background()

    # Logo UPC
    if os.path.exists(logo_path):
        s1.shapes.add_picture(logo_path, Inches(1.0), Inches(0.8), width=Inches(3.2))

    # Badge Carrera
    badge1 = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), Inches(2.2), Inches(5.2), Inches(0.4))
    badge1.fill.solid()
    badge1.fill.fore_color.rgb = RGBColor(30, 41, 59)
    badge1.line.color.rgb = RGBColor(71, 85, 105)
    b1_tf = badge1.text_frame
    b1_p = b1_tf.paragraphs[0]
    b1_p.text = "1ACC0184 - COMPLEJIDAD ALGORÍTMICA | SECCIÓN 4749"
    b1_p.font.name = "Segoe UI"
    b1_p.font.size = Pt(10.5)
    b1_p.font.bold = True
    b1_p.font.color.rgb = RGBColor(226, 232, 240)
    b1_p.alignment = PP_ALIGN.CENTER

    # Main Title
    tb_title = s1.shapes.add_textbox(Inches(1.0), Inches(2.75), Inches(11.3), Inches(1.8))
    t_tf = tb_title.text_frame
    t_tf.word_wrap = True
    tp0 = t_tf.paragraphs[0]
    tp0.text = "Resolución y Validación del Sudoku Generalizado N × N mediante Grafos de Restricciones y Búsqueda Informada"
    tp0.font.name = "Segoe UI"
    tp0.font.size = Pt(27)
    tp0.font.bold = True
    tp0.font.color.rgb = C_WHITE

    tp1 = t_tf.add_paragraph()
    tp1.text = "Informe del Segundo Hito (TB2) — Modelado Topológico, Heurística MRV y Optimización Bitwise O(1)"
    tp1.font.name = "Segoe UI"
    tp1.font.size = Pt(14)
    tp1.font.color.rgb = RGBColor(148, 163, 184)

    # Info card team
    card_team = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), Inches(4.75), Inches(11.3), Inches(2.0))
    card_team.fill.solid()
    card_team.fill.fore_color.rgb = RGBColor(30, 41, 59)
    card_team.line.color.rgb = RGBColor(51, 65, 85)
    
    ct_tf = card_team.text_frame
    ct_tf.margin_left = Inches(0.4)
    ct_tf.margin_top = Inches(0.2)
    
    cp0 = ct_tf.paragraphs[0]
    cp0.text = "INTEGRANTES DEL GRUPO 5 (INGENIERÍA DE SOFTWARE):"
    cp0.font.name = "Segoe UI"
    cp0.font.size = Pt(10.5)
    cp0.font.bold = True
    cp0.font.color.rgb = C_UPC_RED
    
    students = [
        "• Kobashigawa (u202412921) — Fundamentación Teórica y Modelado en Grafos",
        "• Pareja (u202411627) — Motor Algorítmico (MRV + Bitmasks) y Complejidad Big-O",
        "• Riveros (u20241c998) — Ingeniería de Software, GUI Tkinter y Benchmarking Experimental"
    ]
    for st in students:
        p = ct_tf.add_paragraph()
        p.text = st
        p.font.name = "Segoe UI"
        p.font.size = Pt(11)
        p.font.color.rgb = C_WHITE
    
    p_prof = ct_tf.add_paragraph()
    p_prof.text = "PROFESOR: José Luis Soncco Alvarez | CICLO: 2026-20 | Lima, Perú"
    p_prof.font.name = "Segoe UI"
    p_prof.font.size = Pt(10)
    p_prof.font.color.rgb = RGBColor(148, 163, 184)

    # =========================================================================
    # SLIDE 2: CONTEXTO Y DESCRIPCIÓN DEL PROBLEMA
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    add_header(s2, "El Desafío de Escala en Rompecabezas Numéricos (CSP)", "1. Contexto y Problemática", "Kobashigawa", 2)
    
    # Left Card
    c2_1 = add_card(s2, 0.8, 1.45, 5.6, 4.3, "Relevancia en la Industria del Software")
    tb = s2.shapes.add_textbox(Inches(1.05), Inches(2.1), Inches(5.1), Inches(3.4))
    tf = tb.text_frame
    tf.word_wrap = True
    items_s2_left = [
        ("Industria del Entretenimiento Cognitivo:", " Plataformas de videojuegos lógicos (Nintendo Brain Age, Nikoli) requieren validación instantánea de tableros."),
        ("El Límite del Sudoku Clásico:", " En 9 × 9 existen ~6.67 × 10²¹ cuadrículas válidas. Es resoluble mediante heurísticas básicas."),
        ("La Formulación Generalizada N × N:", " Exige evaluar cuadrículas con N = k² (k = 4 → 16×16, k = 7 → 49×49), donde los métodos ingenuos colapsan de forma absoluta."),
        ("Impacto en Sistemas Cloud:", " Validar miles de partidas concurrentes sin optimización agota CPU y dispara costos de infraestructura.")
    ]
    for bold_txt, norm_txt in items_s2_left:
        p = tf.add_paragraph() if tf.paragraphs[0].text else tf.paragraphs[0]
        p.space_after = Pt(10)
        r0 = p.add_run()
        r0.text = "• " + bold_txt
        r0.font.bold = True
        r0.font.size = Pt(11)
        r0.font.color.rgb = C_TEXT_DARK
        r1 = p.add_run()
        r1.text = norm_txt
        r1.font.size = Pt(11)
        r1.font.color.rgb = C_TEXT_MUTED

    # Right Card
    c2_2 = add_card(s2, 6.7, 1.45, 5.8, 4.3, "Explosión Combinatoria y Complejidad")
    tb2 = s2.shapes.add_textbox(Inches(6.95), Inches(2.1), Inches(5.3), Inches(3.4))
    tf2 = tb2.text_frame
    tf2.word_wrap = True
    items_s2_right = [
        ("Fuerza Bruta Inviable:", " Sin poda intermedia, la cantidad de hojas del árbol de decisiones alcanza N^(N²)."),
        ("Magnitud para k = 7 (49 × 49):", " El espacio de estados combinatorial alcanza 49²⁴⁰¹ ≈ 10⁴⁰⁵⁸ estados, superando el número de átomos en el universo observable."),
        ("Solución Requerida:", " Transcender matrices planas y modelar formalmente una red topológica de restricciones binarias que permita podas dinámicas profundas.")
    ]
    for bold_txt, norm_txt in items_s2_right:
        p = tf2.add_paragraph() if tf2.paragraphs[0].text else tf2.paragraphs[0]
        p.space_after = Pt(12)
        r0 = p.add_run()
        r0.text = "• " + bold_txt
        r0.font.bold = True
        r0.font.size = Pt(11.5)
        r0.font.color.rgb = C_TEXT_DARK
        r1 = p.add_run()
        r1.text = norm_txt
        r1.font.size = Pt(11.5)
        r1.font.color.rgb = C_TEXT_MUTED

    # 3 Metrics at bottom
    add_metric_box(s2, 0.8, 5.95, 3.6, 0.95, "O(N^(N²))", "Complejidad Fuerza Bruta", C_UPC_RED)
    add_metric_box(s2, 4.86, 5.95, 3.6, 0.95, "10⁴⁰⁵⁸", "Estados en 49 × 49 (k=7)", C_NAVY)
    add_metric_box(s2, 8.93, 5.95, 3.6, 0.95, "CSP", "Problema de Satisfacción", C_ACCENT_BLUE)

    # =========================================================================
    # SLIDE 3: FUNDAMENTACIÓN TEÓRICA Y NP-COMPLETITUD
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    add_header(s3, "Fundamentación Matemática y NP-Completitud", "1. Marco Teórico", "Kobashigawa", 3)

    c3_1 = add_card(s3, 0.8, 1.45, 5.6, 5.4, "Demostración de Yato & Seta (2003)")
    tb3_1 = s3.shapes.add_textbox(Inches(1.05), Inches(2.1), Inches(5.1), Inches(4.5))
    tf3_1 = tb3_1.text_frame
    tf3_1.word_wrap = True
    
    pts_s3_1 = [
        ("Clase de Complejidad NP-Completo:", " Determinar si una cuadrícula de Sudoku generalizado N × N admite solución es NP-completo."),
        ("Reducción Polinomial Directa:", " La prueba se fundamenta en una reducción desde el problema clásico de Coloración de Grafos (Graph Vertex Coloring):"),
        ("  - Vértices V:", " Cada celda vacía actúa como un nodo del grafo."),
        ("  - Colores C:", " El conjunto de símbolos permitidos {1, ..., N}."),
        ("  - Aristas E:", " Restricciones binarias de diferencia mutua entre pares de celdas que comparten fila, columna o bloque."),
        ("Conclusión Formal:", " No existe algoritmo polinomial determinista conocido; la eficiencia depende críticamente de heurísticas de poda.")
    ]
    for b_txt, n_txt in pts_s3_1:
        p = tf3_1.add_paragraph() if tf3_1.paragraphs[0].text else tf3_1.paragraphs[0]
        p.space_after = Pt(7)
        r0 = p.add_run()
        r0.text = b_txt
        r0.font.bold = True
        r0.font.size = Pt(11)
        r0.font.color.rgb = C_NAVY if "Graph Vertex" in b_txt else C_TEXT_DARK
        r1 = p.add_run()
        r1.text = n_txt
        r1.font.size = Pt(11)
        r1.font.color.rgb = C_TEXT_MUTED

    c3_2 = add_card(s3, 6.7, 1.45, 5.8, 5.4, "Objetivos Específicos del Proyecto")
    tb3_2 = s3.shapes.add_textbox(Inches(6.95), Inches(2.1), Inches(5.3), Inches(4.5))
    tf3_2 = tb3_2.text_frame
    tf3_2.word_wrap = True
    
    objs = [
        ("1. Modelado Topológico de Escala Masiva:", " Representar formalmente las restricciones mediante un grafo de 2,401 nodos y 158,466 aristas, superando holgadamente el umbral de 1,500 nodos exigido en la rúbrica."),
        ("2. Generación Paramétrica y Dataset Reproducible:", " Diseñar un generador sintético en Python 3.12 y pandas exportado en CSV (sudoku_nodes.csv y sudoku_edges.csv) con trazabilidad por integrante."),
        ("3. Algoritmo Híbrido de Alto Rendimiento:", " Integrar Backtracking con heurística informada MRV y operaciones a nivel de bits (Bitmasks O(1)) para lograr tiempos de respuesta en milisegundos."),
        ("4. Aplicativo Interactivo Multi-Escala:", " Implementar una arquitectura desacoplada MVC con interfaz GUI en Tkinter, telemetría en vivo y soporte dinámico de 4×4 a 16×16.")
    ]
    for b_txt, n_txt in objs:
        p = tf3_2.add_paragraph() if tf3_2.paragraphs[0].text else tf3_2.paragraphs[0]
        p.space_after = Pt(10)
        r0 = p.add_run()
        r0.text = b_txt
        r0.font.bold = True
        r0.font.size = Pt(11.5)
        r0.font.color.rgb = C_TEXT_DARK
        r1 = p.add_run()
        r1.text = n_txt
        r1.font.size = Pt(11)
        r1.font.color.rgb = C_TEXT_MUTED

    # =========================================================================
    # SLIDE 4: DATASET Y MODELADO TOPOLÓGICO (|V| = 2,401)
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    add_header(s4, "Dataset y Modelado del Grafo de 2,401 Nodos", "2. Dataset y Topología", "Kobashigawa", 4)

    # Left card info & math
    c4_1 = add_card(s4, 0.8, 1.45, 5.4, 5.4, "Topología y Partición por Integrante")
    tb4 = s4.shapes.add_textbox(Inches(1.05), Inches(2.05), Inches(4.9), Inches(4.6))
    tf4 = tb4.text_frame
    tf4.word_wrap = True
    
    math_items = [
        ("Instancia de Estudio:", " k = 7 → Tablero de N = 49 × 49 celdas."),
        ("Conjunto de Vértices V:", " |V| = N² = 49² = 2,401 nodos (Supera el mínimo de 1,500)."),
        ("Partición Individual (Rúbrica ≥ 500 c/u):", ""),
        ("  • Kobashigawa:", " 800 nodos (Filas 0 a 15)"),
        ("  • Pareja:", " 801 nodos (Filas 16 a 32)"),
        ("  • Riveros:", " 800 nodos (Filas 32 a 48)"),
        ("Grado Regular d(v):", " d(v) = 3N − 2k − 1 = 3(49) − 2(7) − 1 = 132 aristas/nodo."),
        ("Conjunto de Aristas E (Handshaking Lemma):", ""),
        ("  |E| = (|V| × d(v)) / 2 = (2,401 × 132) / 2 =", " 158,466 aristas.")
    ]
    for b_txt, n_txt in math_items:
        p = tf4.add_paragraph() if tf4.paragraphs[0].text else tf4.paragraphs[0]
        p.space_after = Pt(4)
        r0 = p.add_run()
        r0.text = b_txt
        r0.font.bold = True
        r0.font.size = Pt(10.5)
        r0.font.color.rgb = C_UPC_RED if "158,466" in b_txt or "2,401" in b_txt else C_TEXT_DARK
        if n_txt:
            r1 = p.add_run()
            r1.text = n_txt
            r1.font.size = Pt(10.5)
            r1.font.color.rgb = C_TEXT_MUTED

    # Right Card image
    c4_2 = add_card(s4, 6.5, 1.45, 6.0, 5.4, "Visualización del Grafo y Subgrafo de Cliques")
    if os.path.exists(graph_path):
        s4.shapes.add_picture(graph_path, Inches(6.65), Inches(2.1), width=Inches(5.7))

    # =========================================================================
    # SLIDE 5: PROPUESTA ALGORÍTMICA EN 3 NIVELES
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    add_header(s5, "Estrategia de Resolución Progresiva en 3 Niveles", "3. Propuesta Algorítmica", "Pareja", 5)

    col_w = 3.65
    gap = 0.38
    left_start = 0.8

    # Level 1
    c5_1 = add_card(s5, left_start, 1.45, col_w, 5.4, "NIVEL 1: DFS Básico", C_BORDER)
    tb5_1 = s5.shapes.add_textbox(Inches(left_start + 0.2), Inches(2.1), Inches(col_w - 0.4), Inches(4.5))
    tf5_1 = tb5_1.text_frame
    tf5_1.word_wrap = True
    p = tf5_1.paragraphs[0]
    p.text = "Línea Base Convencional\n"
    p.font.bold = True
    p.font.size = Pt(12)
    p.font.color.rgb = C_TEXT_DARK
    items_l1 = [
        "Búsqueda exhaustiva celda por celda en orden lexicográfico secuencial.",
        "Comprobación por bucles iterativos convencionales en O(N) por intento.",
        "Ausencia de heurística: explora subárboles enteros antes de detectar inconsistencias.",
        "Tiempo en prueba: 38,074 ms con 1.89M de retrocesos."
    ]
    for it in items_l1:
        p = tf5_1.add_paragraph()
        p.text = "• " + it
        p.font.size = Pt(10.5)
        p.font.color.rgb = C_TEXT_MUTED
        p.space_after = Pt(8)

    # Level 2
    c5_2 = add_card(s5, left_start + col_w + gap, 1.45, col_w, 5.4, "NIVEL 2: DFS + MRV", C_ACCENT_BLUE)
    tb5_2 = s5.shapes.add_textbox(Inches(left_start + col_w + gap + 0.2), Inches(2.1), Inches(col_w - 0.4), Inches(4.5))
    tf5_2 = tb5_2.text_frame
    tf5_2.word_wrap = True
    p = tf5_2.paragraphs[0]
    p.text = "Poda Informada (AI)\n"
    p.font.bold = True
    p.font.size = Pt(12)
    p.font.color.rgb = C_ACCENT_BLUE
    items_l2 = [
        "Heurística MRV (Minimum Remaining Values, Russell & Norvig).",
        "Selecciona dinámicamente la variable con menor dominio legal |D(v)|.",
        "Poda inmediata de callejones sin salida (Dead-end pruning) ante |D(v)| = 0.",
        "Reducción del 99.23% del espacio de búsqueda inútil (14,672 backtracks)."
    ]
    for it in items_l2:
        p = tf5_2.add_paragraph()
        p.text = "• " + it
        p.font.size = Pt(10.5)
        p.font.color.rgb = C_TEXT_MUTED
        p.space_after = Pt(8)

    # Level 3
    c5_3 = add_card(s5, left_start + (col_w + gap)*2, 1.45, col_w, 5.4, "NIVEL 3: MRV + Bitmasks", C_SUCCESS)
    tb5_3 = s5.shapes.add_textbox(Inches(left_start + (col_w + gap)*2 + 0.2), Inches(2.1), Inches(col_w - 0.4), Inches(4.5))
    tf5_3 = tb5_3.text_frame
    tf5_3.word_wrap = True
    p = tf5_3.paragraphs[0]
    p.text = "Optimización en Hardware\n"
    p.font.bold = True
    p.font.size = Pt(12)
    p.font.color.rgb = C_SUCCESS
    items_l3 = [
        "Representación de dominios en registros de procesador mediante vectores de bits.",
        "Operaciones bitwise O(1): AND (&), OR (|) y NOT (~).",
        "Instrucción de CPU POPCNT (bit_count) para contar candidatos en 1 ciclo de reloj.",
        "Tiempo récord: 147.44 ms (Aceleración global de 258.2× respecto a Nivel 1)."
    ]
    for it in items_l3:
        p = tf5_3.add_paragraph()
        p.text = "• " + it
        p.font.size = Pt(10.5)
        p.font.color.rgb = C_TEXT_MUTED
        p.space_after = Pt(8)

    # =========================================================================
    # SLIDE 6: HEURÍSTICA MRV Y PRINCIPIO FAIL-FIRST
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    add_header(s6, "Heurística MRV y Principio de 'Fallar Primero'", "3. Heurística de Poda", "Pareja", 6)

    c6_1 = add_card(s6, 0.8, 1.45, 5.6, 5.4, "Formulación Matemática de MRV")
    tb6_1 = s6.shapes.add_textbox(Inches(1.05), Inches(2.1), Inches(5.1), Inches(4.5))
    tf6_1 = tb6_1.text_frame
    tf6_1.word_wrap = True
    pts_s6_1 = [
        ("Definición Formal:", " En lugar de seleccionar celdas secuencialmente (r, c), MRV evalúa todas las celdas vacías y elige la más restringida:"),
        ("  v* = arg min |D(v)|", " para todo v ∈ V_vacíos"),
        ("Principio 'Fail-First':", " Si una celda tiene solo 1 opción legal (singleton), se debe asignar de inmediato. Si tiene 0 opciones (|D(v)| = 0), el estado es inconsistente."),
        ("Poda Temprana de Callejón sin Salida:", " Al detectar |D(v)| = 0, el solver aborta de raíz el subárbol, ahorrándose explorar hasta O(N^(m-1)) nodos inválidos."),
        ("Preservación de Solución:", " MRV nunca descarta ramas viables; garantiza la misma solución que el método exhaustivo pero podando ramas muertas.")
    ]
    for b_txt, n_txt in pts_s6_1:
        p = tf6_1.add_paragraph() if tf6_1.paragraphs[0].text else tf6_1.paragraphs[0]
        p.space_after = Pt(8)
        r0 = p.add_run()
        r0.text = b_txt
        r0.font.bold = True
        r0.font.size = Pt(11)
        r0.font.color.rgb = C_ACCENT_BLUE if "arg min" in b_txt else C_TEXT_DARK
        r1 = p.add_run()
        r1.text = n_txt
        r1.font.size = Pt(11)
        r1.font.color.rgb = C_TEXT_MUTED

    c6_2 = add_card(s6, 6.7, 1.45, 5.8, 5.4, "Impacto en el Árbol de Búsqueda")
    tb6_2 = s6.shapes.add_textbox(Inches(6.95), Inches(2.1), Inches(5.3), Inches(4.5))
    tf6_2 = tb6_2.text_frame
    tf6_2.word_wrap = True
    pts_s6_2 = [
        ("Factor de Ramificación Efectivo (Beff):", " En búsqueda ciega, el factor de ramificación es B ≈ N (9 opciones por paso). Con MRV, colapsa a Beff ≈ 1.2."),
        ("Eliminación del 99.23% del Árbol:", " En la prueba de estrés, los retrocesos cayeron de 1,897,847 a solo 14,672 backtracks."),
        ("Sobrecosto Local vs Ganancia Global:", " Calcular dominios cuesta O(m · N), pero ahorra millones de operaciones de exploración profunda inútil."),
        ("Demostración Empírica:", " Comprobado tanto en Sudokus 9×9 estándar como en configuraciones multiescala de 16×16.")
    ]
    for b_txt, n_txt in pts_s6_2:
        p = tf6_2.add_paragraph() if tf6_2.paragraphs[0].text else tf6_2.paragraphs[0]
        p.space_after = Pt(10)
        r0 = p.add_run()
        r0.text = "• " + b_txt
        r0.font.bold = True
        r0.font.size = Pt(11.5)
        r0.font.color.rgb = C_TEXT_DARK
        r1 = p.add_run()
        r1.text = n_txt
        r1.font.size = Pt(11)
        r1.font.color.rgb = C_TEXT_MUTED

    # =========================================================================
    # SLIDE 7: OPTIMIZACIÓN A BAJO NIVEL: BITMASKS EN O(1)
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    add_header(s7, "Optimización de Bajo Nivel: Bitmasks y Hardware POPCNT", "3. Aceleración por Hardware", "Pareja", 7)

    c7_1 = add_card(s7, 0.8, 1.45, 5.6, 5.4, "Lógica Binaria y Vectores de Bits")
    tb7_1 = s7.shapes.add_textbox(Inches(1.05), Inches(2.1), Inches(5.1), Inches(4.5))
    tf7_1 = tb7_1.text_frame
    tf7_1.word_wrap = True
    pts_s7_1 = [
        ("Máscaras por Región:", " Tres arreglos de enteros de N bits: row_masks[r], col_masks[c] y box_masks[b]. El bit v está en 1 si el valor ya fue usado."),
        ("Unión de Restricciones en 1 Ciclo:", ""),
        ("  usados = row_masks[r] | col_masks[c] | box_masks[b]", ""),
        ("Valores Admisibles Inmediatos:", ""),
        ("  disponibles = all_mask & (~usados)", ""),
        ("Cero Bucles de Inspección:", " No se itera sobre celdas ni se crean colecciones temporales en memoria."),
        ("Persistencia Asíncrona:", " Asignar o desasignar un valor equivale a conmutar un bit con XOR (^= (1 << v)).")
    ]
    for b_txt, n_txt in pts_s7_1:
        p = tf7_1.add_paragraph() if tf7_1.paragraphs[0].text else tf7_1.paragraphs[0]
        p.space_after = Pt(6)
        r0 = p.add_run()
        r0.text = b_txt
        r0.font.bold = True
        r0.font.size = Pt(10.5)
        r0.font.color.rgb = C_SUCCESS if "disponibles" in b_txt or "usados" in b_txt else C_TEXT_DARK
        if n_txt:
            r1 = p.add_run()
            r1.text = n_txt
            r1.font.size = Pt(10.5)
            r1.font.color.rgb = C_TEXT_MUTED

    c7_2 = add_card(s7, 6.7, 1.45, 5.8, 5.4, "Instrucción de CPU POPCNT y Rendimiento")
    tb7_2 = s7.shapes.add_textbox(Inches(6.95), Inches(2.1), Inches(5.3), Inches(4.5))
    tf7_2 = tb7_2.text_frame
    tf7_2.word_wrap = True
    pts_s7_2 = [
        ("Instrucción POPCNT (Population Count):", " La función int.bit_count() en Python 3.12 mapea directamente a la instrucción nativa POPCNT de los procesadores x86-64 y ARM."),
        ("Conteo en O(1) Estricto:", " Contar cuántos candidatos le quedan a una celda se ejecuta en un solo ciclo de reloj de hardware, reduciendo la constante asintótica de O(N) a O(1)."),
        ("Identidad de Trayectoria:", " Nivel 2 y Nivel 3 toman exactamente las mismas 14,672 decisiones lógicas."),
        ("Ganancia de Velocidad Pura:", " El tiempo colapsa de 3,571.31 ms a tan solo 147.44 ms (Aceleración de 24.2× sobre MRV tradicional y 258.2× global).")
    ]
    for b_txt, n_txt in pts_s7_2:
        p = tf7_2.add_paragraph() if tf7_2.paragraphs[0].text else tf7_2.paragraphs[0]
        p.space_after = Pt(10)
        r0 = p.add_run()
        r0.text = "• " + b_txt
        r0.font.bold = True
        r0.font.size = Pt(11.5)
        r0.font.color.rgb = C_TEXT_DARK
        r1 = p.add_run()
        r1.text = n_txt
        r1.font.size = Pt(11)
        r1.font.color.rgb = C_TEXT_MUTED

    # =========================================================================
    # SLIDE 8: ANÁLISIS ASINTÓTICO DE COMPLEJIDAD (BIG-O)
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    add_header(s8, "Análisis Asintótico de Complejidad Temporal y Espacial", "4. Análisis de Complejidad", "Pareja", 8)

    c8_1 = add_card(s8, 0.8, 1.45, 5.6, 5.4, "Complejidad Temporal Asintótica Big-O")
    tb8_1 = s8.shapes.add_textbox(Inches(1.05), Inches(2.1), Inches(5.1), Inches(4.5))
    tf8_1 = tb8_1.text_frame
    tf8_1.word_wrap = True
    t_items = [
        ("Fuerza Bruta / Sin Poda:", " O(N^(N²)) — Completamente intratable."),
        ("Nivel 1 (Backtracking Básico DFS):", ""),
        ("  T_básico(N) = O(N · N^m) = O(N^(m+1))", " en peor caso, donde m es el número de celdas vacías iniciales (m ≤ N²)."),
        ("Nivel 2 (DFS + Heurística MRV):", ""),
        ("  T_mrv(N) = O(m · N) + O(Beff^d)", " donde Beff ≈ 1.2 (factor de ramificación efectivo colapsado)."),
        ("Nivel 3 (MRV + Bitmasks O(1)):", ""),
        ("  T_bitmask(N) = O(m · 1) + O(Beff^d)", " — Mismo árbol que Nivel 2 pero con costo de verificación por nodo en O(1) de hardware.")
    ]
    for b_txt, n_txt in t_items:
        p = tf8_1.add_paragraph() if tf8_1.paragraphs[0].text else tf8_1.paragraphs[0]
        p.space_after = Pt(7)
        r0 = p.add_run()
        r0.text = b_txt
        r0.font.bold = True
        r0.font.size = Pt(11)
        r0.font.color.rgb = C_NAVY if "T_" in b_txt else C_TEXT_DARK
        if n_txt:
            r1 = p.add_run()
            r1.text = n_txt
            r1.font.size = Pt(10.5)
            r1.font.color.rgb = C_TEXT_MUTED

    c8_2 = add_card(s8, 6.7, 1.45, 5.8, 5.4, "Complejidad Espacial y Estructuras en Memoria")
    tb8_2 = s8.shapes.add_textbox(Inches(6.95), Inches(2.1), Inches(5.3), Inches(4.5))
    tf8_2 = tb8_2.text_frame
    tf8_2.word_wrap = True
    s_items = [
        ("Lista de Adyacencia vs Matriz de Adyacencia:", ""),
        ("  • Matriz de Adyacencia:", " Requeriría |V|² = 2401² ≈ 5.76 millones de casillas (densidad de apenas 5.5%, enorme desperdicio)."),
        ("  • Lista de Adyacencia (Set):", " Almacena solo conexiones reales: O(|V| + |E|) ≈ 160,867 elementos en memoria RAM (apenas ~1.25 MB)."),
        ("Pila de Recursión (Call Stack):", " Cada llamada asigna 1 celda vacía y nunca revisita nodos. Profundidad máxima Dmax ≤ N²."),
        ("Memoria Total del Sistema:", " S(N) = O(N²)"),
        ("Garantía de Estabilidad:", " Consumo en RAM de pocos kilobytes para el solver, garantizando cero riesgo de Stack Overflow.")
    ]
    for b_txt, n_txt in s_items:
        p = tf8_2.add_paragraph() if tf8_2.paragraphs[0].text else tf8_2.paragraphs[0]
        p.space_after = Pt(7)
        r0 = p.add_run()
        r0.text = b_txt
        r0.font.bold = True
        r0.font.size = Pt(11)
        r0.font.color.rgb = C_UPC_RED if "S(N)" in b_txt else C_TEXT_DARK
        if n_txt:
            r1 = p.add_run()
            r1.text = n_txt
            r1.font.size = Pt(10.5)
            r1.font.color.rgb = C_TEXT_MUTED

    # =========================================================================
    # SLIDE 9: ARQUITECTURA DE SOFTWARE Y MODELADO UML
    # =========================================================================
    s9 = prs.slides.add_slide(blank_layout)
    add_header(s9, "Arquitectura del Sistema y Diagrama de Clases UML", "4. Ingeniería de Software", "Riveros", 9)

    c9_1 = add_card(s9, 0.8, 1.45, 5.4, 5.4, "Patrón Arquitectónico Desacoplado MVC")
    tb9_1 = s9.shapes.add_textbox(Inches(1.05), Inches(2.05), Inches(4.9), Inches(4.6))
    tf9_1 = tb9_1.text_frame
    tf9_1.word_wrap = True
    arch_items = [
        ("Capa Vista (GUI Tkinter):", " src/main.py administra la interfaz visual interactiva, eventos de usuario y telemetría en tiempo real."),
        ("Capa Modelo (Grafo y Tablero):", " src/model.py implementa ConstraintGraph y SudokuBoard, separando la topología de las restricciones del estado de juego."),
        ("Capa Controlador (Solvers):", " src/solver.py encapsula los tres niveles algorítmicos bajo la fachada SudokuSolver."),
        ("Relación de Agregación:", " SudokuBoard agrega un ConstraintGraph; un mismo grafo en memoria puede ser compartido por múltiples partidas sin recargar."),
        ("Estándares IEEE 830 / ISO 29148:", " 7 Requerimientos Funcionales (RF-01 a RF-07) y 4 No Funcionales (RNF-01 a RNF-04: latencia <100ms, 60 FPS).")
    ]
    for b_txt, n_txt in arch_items:
        p = tf9_1.add_paragraph() if tf9_1.paragraphs[0].text else tf9_1.paragraphs[0]
        p.space_after = Pt(8)
        r0 = p.add_run()
        r0.text = "• " + b_txt
        r0.font.bold = True
        r0.font.size = Pt(11)
        r0.font.color.rgb = C_TEXT_DARK
        r1 = p.add_run()
        r1.text = n_txt
        r1.font.size = Pt(10.5)
        r1.font.color.rgb = C_TEXT_MUTED

    c9_2 = add_card(s9, 6.5, 1.45, 6.0, 5.4, "Diagrama de Clases UML del Sistema")
    if os.path.exists(uml_path):
        s9.shapes.add_picture(uml_path, Inches(6.65), Inches(2.1), width=Inches(5.7))

    # =========================================================================
    # SLIDE 10: INTERFAZ GRÁFICA Y CASOS DE USO
    # =========================================================================
    s10 = prs.slides.add_slide(blank_layout)
    add_header(s10, "Demostración de la Interfaz Gráfica y Casos de Uso", "4. Aplicativo Interactivo", "Riveros", 10)

    c10_1 = add_card(s10, 0.8, 1.45, 5.4, 5.4, "Casos de Uso Principales (Roadmap)")
    tb10_1 = s10.shapes.add_textbox(Inches(1.05), Inches(2.05), Inches(4.9), Inches(4.6))
    tf10_1 = tb10_1.text_frame
    tf10_1.word_wrap = True
    cu_items = [
        ("CU-01: Juego Manual y Verificación de Reglas:", " El usuario introduce dígitos; al presionar 'Comprobar Solución', se consulta conflicts() e ilumina conflictos en rojo bermellón (#D0021B)."),
        ("CU-02: Resolución Asistida y Benchmarking:", " Ejecución inmediata del solver; las celdas halladas se colorean en azul marino (#003366) y el panel de telemetría reporta tiempo, nodos y podas."),
        ("Persistencia y Restauración Automática:", " Cambiar de algoritmo en el combobox restaura de inmediato las pistas originales para una comparación 100% justa sobre el mismo puzzle."),
        ("CU-03: Soporte Multi-Escala Dinámico:", " Redimensionamiento reactivo en tiempo real para 4×4 (k=2), 9×9 (k=3) y 16×16 (k=4, 256 celdas).")
    ]
    for b_txt, n_txt in cu_items:
        p = tf10_1.add_paragraph() if tf10_1.paragraphs[0].text else tf10_1.paragraphs[0]
        p.space_after = Pt(10)
        r0 = p.add_run()
        r0.text = "• " + b_txt
        r0.font.bold = True
        r0.font.size = Pt(11)
        r0.font.color.rgb = C_TEXT_DARK
        r1 = p.add_run()
        r1.text = n_txt
        r1.font.size = Pt(10.5)
        r1.font.color.rgb = C_TEXT_MUTED

    # Right: GUI Screenshots
    c10_2 = add_card(s10, 6.5, 1.45, 6.0, 5.4, "Capturas del Software en Ejecución")
    if os.path.exists(gui_board_path):
        s10.shapes.add_picture(gui_board_path, Inches(6.65), Inches(2.0), width=Inches(3.3))
    if os.path.exists(gui_4x4_path):
        s10.shapes.add_picture(gui_4x4_path, Inches(10.1), Inches(2.0), width=Inches(2.25))
    if os.path.exists(gui_16x16_path):
        s10.shapes.add_picture(gui_16x16_path, Inches(6.65), Inches(4.55), width=Inches(5.7))

    # =========================================================================
    # SLIDE 11: VALIDACIÓN EXPERIMENTAL Y BENCHMARKING (21 PISTAS)
    # =========================================================================
    s11 = prs.slides.add_slide(blank_layout)
    add_header(s11, "Validación Experimental: Benchmarking de 21 Pistas", "5. Validación y Pruebas", "Riveros", 11)

    # Table Card
    c11_table = add_card(s11, 0.8, 1.45, 11.733, 2.7, "Tabla 1: Comparativa de Rendimiento sobre Instancia de Alta Dificultad (21 Pistas)")
    
    # Add native PowerPoint table
    table_shape = s11.shapes.add_table(4, 6, Inches(1.0), Inches(2.05), Inches(11.333), Inches(1.8))
    t = table_shape.table
    
    col_widths = [Inches(1.6), Inches(3.6), Inches(1.8), Inches(1.5), Inches(1.5), Inches(1.333)]
    for i, w in enumerate(col_widths):
        t.columns[i].width = w
        
    headers = ["Nivel", "Estrategia Algorítmica", "Tiempo (ms)", "Nodos", "Backtracks", "Poda (%)"]
    data = [
        ["Nivel 1", "Backtracking Básico (DFS Secuencial)", "38,074.28 ms", "1,897,847", "1,897,847", "Línea Base"],
        ["Nivel 2", "Backtracking con Heurística MRV Clásica", "3,571.31 ms", "14,672", "14,672", "-99.23%"],
        ["Nivel 3", "Backtracking con MRV + Bitmasks O(1)", "147.44 ms", "14,672", "14,672", "-99.23%"]
    ]
    
    for c_idx, h in enumerate(headers):
        cell = t.cell(0, c_idx)
        cell.fill.solid()
        cell.fill.fore_color.rgb = C_NAVY
        p = cell.text_frame.paragraphs[0]
        p.text = h
        p.font.name = "Segoe UI"
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = C_WHITE
        p.alignment = PP_ALIGN.CENTER
        
    for r_idx, row in enumerate(data):
        for c_idx, val in enumerate(row):
            cell = t.cell(r_idx + 1, c_idx)
            cell.fill.solid()
            cell.fill.fore_color.rgb = RGBColor(248, 250, 252) if r_idx % 2 == 0 else C_WHITE
            p = cell.text_frame.paragraphs[0]
            p.text = val
            p.font.name = "Segoe UI"
            p.font.size = Pt(10.5)
            p.font.color.rgb = C_SUCCESS if "-99.23%" in val or "147.44" in val else C_TEXT_DARK
            p.font.bold = True if r_idx == 2 or c_idx == 0 else False
            p.alignment = PP_ALIGN.CENTER if c_idx not in [1] else PP_ALIGN.LEFT

    # Metric boxes below table
    add_metric_box(s11, 0.8, 4.35, 3.7, 1.25, "-99.23%", "Poda Combinatoria con MRV", C_UPC_RED)
    add_metric_box(s11, 4.816, 4.35, 3.7, 1.25, "14,672", "Identidad Exacta de Decisiones (N2 = N3)", C_NAVY)
    add_metric_box(s11, 8.833, 4.35, 3.7, 1.25, "258.2×", "Aceleración Global (Nivel 1 vs Nivel 3)", C_SUCCESS)

    # Bottom summary card
    c11_sum = add_card(s11, 0.8, 5.75, 11.733, 1.15, "")
    tb_sum = s11.shapes.add_textbox(Inches(1.0), Inches(5.82), Inches(11.333), Inches(0.95))
    tf_sum = tb_sum.text_frame
    tf_sum.word_wrap = True
    p = tf_sum.paragraphs[0]
    p.text = "Interpretación Clave de Resultados:"
    p.font.bold = True
    p.font.size = Pt(11)
    p.font.color.rgb = C_NAVY
    p1 = tf_sum.add_paragraph()
    p1.text = "1) MRV reduce el árbol en 99.23% (de 1.89 millones a 14,672 retrocesos). 2) La lógica de poda es idéntica entre Nivel 2 y Nivel 3 (mismos backtracks). 3) Bitmasks ejecuta en hardware en O(1), reduciendo el tiempo de 3.5 segundos a solo 147 milisegundos (258× más rápido)."
    p1.font.size = Pt(10.5)
    p1.font.color.rgb = C_TEXT_DARK

    # =========================================================================
    # SLIDE 12: CONCLUSIONES Y TRABAJO FUTURO
    # =========================================================================
    s12 = prs.slides.add_slide(blank_layout)
    add_header(s12, "Conclusiones del Proyecto y Proyección Académica", "6. Conclusiones", "Riveros", 12)

    c12_1 = add_card(s12, 0.8, 1.45, 11.733, 1.6, "1. Eficiencia y Escalabilidad del Modelado en Grafos", C_BORDER)
    tb12_1 = s12.shapes.add_textbox(Inches(1.05), Inches(1.95), Inches(11.2), Inches(1.0))
    tf12_1 = tb12_1.text_frame
    tf12_1.word_wrap = True
    p = tf12_1.paragraphs[0]
    p.text = "El modelado del Sudoku generalizado mediante un grafo regular simple de escala masiva (|V| = 2,401 y |E| = 158,466 para k=7) demostró que abstraer las restricciones a listas de adyacencia (set) permite verificar colisiones en tiempo O(1) promedio y memoria O(|V| + |E|) (~1.25 MB en RAM), superando la ineficiencia de matrices densas y cumpliendo con holgura las cuotas individuales de 800 nodos por integrante."
    p.font.size = Pt(11)
    p.font.color.rgb = C_TEXT_DARK

    c12_2 = add_card(s12, 0.8, 3.2, 11.733, 1.6, "2. Impacto Algorítmico: Heurística MRV y Aceleración por Hardware", C_BORDER)
    tb12_2 = s12.shapes.add_textbox(Inches(1.05), Inches(3.7), Inches(11.2), Inches(1.0))
    tf12_2 = tb12_2.text_frame
    tf12_2.word_wrap = True
    p = tf12_2.paragraphs[0]
    p.text = "La experimentación demostró que la búsqueda ciega (Nivel 1) colapsa ante la explosión combinatoria (1.89 millones de backtracks). La heurística informada MRV (Nivel 2) eliminó el 99.23% del espacio de búsqueda inútil al podar callejones sin salida tempranos. Las Máscaras de Bits (Nivel 3) explotaron la instrucción POPCNT de la CPU para alcanzar 147.44 ms y una aceleración global de 258.2×."
    p.font.size = Pt(11)
    p.font.color.rgb = C_TEXT_DARK

    c12_3 = add_card(s12, 0.8, 4.95, 11.733, 1.9, "3. Ingeniería del Software y Proyección al Hito 3", C_ACCENT_BLUE)
    tb12_3 = s12.shapes.add_textbox(Inches(1.05), Inches(5.45), Inches(11.2), Inches(1.2))
    tf12_3 = tb12_3.text_frame
    tf12_3.word_wrap = True
    p = tf12_3.paragraphs[0]
    p.text = "La arquitectura modular desacoplada articuló exitosamente la GUI interactiva (main.py), la capa de datos (model.py) y el motor de búsqueda (solver.py), cumpliendo los estándares de adaptabilidad multi-escala (4×4, 9×9 y 16×16) y telemetría en vivo. Como trabajo a futuro para el Hito 3, se proyecta incorporar propagación por consistencia de arcos (algoritmo AC-3) y ordenamiento heurístico de valores (LCV) para órdenes mayores (N ≥ 25)."
    p.font.size = Pt(11)
    p.font.color.rgb = C_TEXT_DARK

    # =========================================================================
    # SLIDE 13: CIERRE Y RONDA DE PREGUNTAS
    # =========================================================================
    s13 = prs.slides.add_slide(blank_layout)
    bg13 = s13.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5))
    bg13.fill.solid()
    bg13.fill.fore_color.rgb = C_DARK_BG
    bg13.line.fill.background()

    # Red accent stripe top
    s13.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(0.12)).fill.solid()
    s13.shapes[-1].fill.fore_color.rgb = C_UPC_RED
    s13.shapes[-1].line.fill.background()

    # Title Thank you
    tb_ty = s13.shapes.add_textbox(Inches(1.0), Inches(1.2), Inches(11.333), Inches(1.5))
    tf_ty = tb_ty.text_frame
    p = tf_ty.paragraphs[0]
    p.text = "¡Muchas Gracias por su Atención!"
    p.font.name = "Segoe UI"
    p.font.size = Pt(36)
    p.font.bold = True
    p.font.color.rgb = C_WHITE
    p.alignment = PP_ALIGN.CENTER
    
    p_sub = tf_ty.add_paragraph()
    p_sub.text = "Sesión de Sustentación y Ronda de Preguntas con el Docente"
    p_sub.font.name = "Segoe UI"
    p_sub.font.size = Pt(16)
    p_sub.font.color.rgb = RGBColor(148, 163, 184)
    p_sub.alignment = PP_ALIGN.CENTER

    # Card Links and Team
    card13 = s13.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.5), Inches(2.9), Inches(10.333), Inches(3.8))
    card13.fill.solid()
    card13.fill.fore_color.rgb = RGBColor(30, 41, 59)
    card13.line.color.rgb = RGBColor(51, 65, 85)
    
    c13_tf = card13.text_frame
    c13_tf.margin_left = Inches(0.5)
    c13_tf.margin_top = Inches(0.3)
    
    p = c13_tf.paragraphs[0]
    p.text = "REPOSITORIO INSTITUCIONAL GITHUB (CÓDIGO Y DATASET):"
    p.font.bold = True
    p.font.size = Pt(12)
    p.font.color.rgb = C_UPC_RED
    
    p_link = c13_tf.add_paragraph()
    p_link.text = "https://github.com/upc-pre-202610-1acc0184-4749-grupo-5/busqueda-rutas-app"
    p_link.font.bold = True
    p_link.font.size = Pt(13)
    p_link.font.color.rgb = RGBColor(56, 189, 248) # Cyan link
    p_link.space_after = Pt(14)

    p_dt = c13_tf.add_paragraph()
    p_dt.text = "Recursos Disponibles en el Repositorio:"
    p_dt.font.bold = True
    p_dt.font.size = Pt(11.5)
    p_dt.font.color.rgb = C_WHITE
    
    resources = [
        "• Código fuente completo: src/main.py (GUI), src/model.py (Grafo) y src/solver.py (Algoritmos).",
        "• Banco de pruebas CSV: dataset/sudoku_nodes.csv (2,401 nodos) y dataset/sudoku_edges.csv (158,466 aristas).",
        "• Suite de pruebas unitarias automatizadas con cobertura del 100% (tests/test_model.py)."
    ]
    for r in resources:
        pr = c13_tf.add_paragraph()
        pr.text = r
        pr.font.size = Pt(11)
        pr.font.color.rgb = RGBColor(226, 232, 240)
        pr.space_after = Pt(4)

    output_path = r"C:\Users\marsr\busqueda-rutas-app\report\Exposicion_TB2_Complejidad_Algoritmica_Grupo5.pptx"
    prs.save(output_path)
    print(f"Presentation saved successfully at: {output_path}")

if __name__ == "__main__":
    build_presentation()
