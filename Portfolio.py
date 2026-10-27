import streamlit as st
import base64
import os

# ==========================================
# KONFIGURACJA STRONY (Z WYMUSZONYM JASNYM MOTYWEM)
# ==========================================
st.set_page_config(page_title="Damian Kubiak | Portfolio", layout="wide", initial_sidebar_state="expanded")

# ==========================================
# STAŁE NAWIGACYJNE
# ==========================================
TAB_OMNIE = "omnie"
TAB_KLIMAT = "klimat"
TAB_ZBIORNIK = "zbiornik"
TAB_CPTU = "cptu"

PROGRAMY_DICT = {
    TAB_KLIMAT: "Generator Obciążeń Klimatycznych",
    TAB_ZBIORNIK: "Posadowienie Pośrednie Zbiornika",
    TAB_CPTU: "Analiza sondowań CPTU"
}

# ==========================================
# FUNKCJA DO ŁADOWANIA LOKALNEGO TŁA
# ==========================================
def pobierz_tlo_base64(nazwa_pliku):
    if os.path.exists(nazwa_pliku):
        with open(nazwa_pliku, "rb") as image_file:
            kod_base64 = base64.b64encode(image_file.read()).decode()
            rozszerzenie = nazwa_pliku.split('.')[-1].lower()
            mime = f"image/{rozszerzenie}" if rozszerzenie != 'jpg' else "image/jpeg"
            return f"data:{mime};base64,{kod_base64}"
    return None 

NAZWA_PLIKU = "tło.png" 
tlo_url = pobierz_tlo_base64(NAZWA_PLIKU)

# ==========================================
# GLOBALNY DESIGN SYSTEM (CSS)
# ==========================================
st.markdown("""
<style>
/* Wymuszenie podstawowych kolorów dla jasnego motywu niezależnie od ustawień chmury */
:root {
    --ink: #151515;
    --muted: #666;
    --paper: #f4f1ea;
    --card: rgba(255,255,255,0.86);
    --line: rgba(21,21,21,0.13);
    --accent: #b56b35;
}

/* Główne tło i tekst aplikacji */
.stApp {
    color: var(--ink) !important;
    background:
        radial-gradient(circle at 85% 10%, rgba(181,107,53,.10), transparent 30%),
        linear-gradient(135deg, #f7f5ef 0%, #eeeae1 100%) !important;
}

[data-testid="stAppViewContainer"] > .main {
    background: transparent !important;
}

header[data-testid="stHeader"] {
    background: transparent !important;
}

.block-container {
    max-width: 1220px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

/* Ciemny panel boczny - naprawiony dla chmury */
[data-testid="stSidebar"] {
    background-color: #171717 !important;
    border-right: 1px solid rgba(255,255,255,.08) !important;
}

[data-testid="stSidebar"] * {
    color: #f4f1ea !important;
}

[data-testid="stSidebar"] [data-testid="stRadio"] label span {
    font-size: 1rem !important;
    line-height: 1.45 !important;
}

/* Przyciski nawigacyjne w menu bocznym */
[data-testid="stSidebar"] [data-testid="stButton"] > button {
    justify-content: flex-start !important;
    padding-left: 14px !important;
    border-radius: 8px !important;
    border: 1px solid rgba(255,255,255,.10) !important;
    background-color: rgba(255,255,255,.06) !important;
    color: #f4f1ea !important;
}

[data-testid="stSidebar"] [data-testid="stButton"] > button p,
[data-testid="stSidebar"] [data-testid="stButton"] > button div {
    text-align: left !important;
    font-size: 1rem !important;
    font-weight: 600 !important;
    color: #f4f1ea !important;
}

h1, h2, h3 {
    letter-spacing: -0.035em;
    color: var(--ink) !important;
}

h1 { font-weight: 750 !important; }
h2, h3 { font-weight: 700 !important; }
p, li { line-height: 1.7; color: var(--ink) !important; }

/* Stylizacja Głównych Przycisków (Zobacz Projekt) - NAPRAWA CZARNYCH PROSTOKĄTÓW */
div[data-testid="stButton"] > button {
    border-radius: 8px !important;
    font-weight: 700 !important;
    min-height: 44px !important;
    background-color: rgba(255,255,255,0.7) !important;
    color: #151515 !important;
    border: 1px solid var(--line) !important;
    transition: all 0.2s ease !important;
}

div[data-testid="stButton"] > button:hover {
    background-color: rgba(255,255,255,1) !important;
    border-color: var(--accent) !important;
    color: var(--accent) !important;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05) !important;
}

div[data-testid="stButton"] > button p {
    color: inherit !important;
}

/* NAPRAWA ZAKŁADEK (Tabs) W CHMURZE */
.stTabs [data-baseweb="tab-list"] {
    gap: 8px;
    border-bottom: 1px solid var(--line);
    background: transparent !important;
}

.stTabs [data-baseweb="tab"] {
    padding: 10px 16px;
    background: transparent !important;
}

/* Twarde wymuszenie czarnego tekstu na zakładkach */
.stTabs [data-baseweb="tab"] p, 
.stTabs [data-baseweb="tab"] span,
.stTabs [data-baseweb="tab"] div {
    color: #1a1a1a !important; 
    font-weight: 700 !important;
    font-size: 1.05rem !important;
}

/* Aktywna zakładka (podkreślenie i kolor) */
.stTabs [aria-selected="true"] {
    border-bottom: 2px solid var(--accent) !important;
}
.stTabs [aria-selected="true"] p, 
.stTabs [aria-selected="true"] span {
    color: var(--accent) !important;
}


/* Kafelki Portfolio */
.portfolio-card {
    background: var(--card);
    border: 1px solid var(--line);
    border-radius: 16px;
    padding: 28px;
    box-shadow: 0 10px 35px rgba(0,0,0,.06);
    backdrop-filter: blur(8px);
    margin-bottom: 15px;
}

.project-kicker {
    color: var(--accent);
    font-size: .78rem;
    font-weight: 800;
    letter-spacing: .14em;
    text-transform: uppercase;
    margin-bottom: 8px;
}

.project-title {
    font-size: 1.65rem;
    font-weight: 760;
    line-height: 1.12;
    margin-bottom: 10px;
    color: var(--ink) !important;
}

.project-description {
    color: #444 !important;
    font-size: 1rem;
    line-height: 1.65;
}

.metric-card {
    background: rgba(255,255,255,.72);
    border: 1px solid var(--line);
    border-radius: 12px;
    padding: 18px;
    min-height: 105px;
}

.metric-label {
    color: #777 !important;
    font-size: .76rem;
    font-weight: 750;
    letter-spacing: .10em;
    text-transform: uppercase;
}

.metric-value {
    color: var(--ink) !important;
    font-size: 1.15rem;
    font-weight: 750;
    margin-top: 5px;
}

@media (max-width: 768px) {
    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
    }
    .portfolio-card {
        padding: 20px;
    }
    .project-title {
        font-size: 1.35rem;
    }
}
</style>
""", unsafe_allow_html=True)

# ==========================================
# ZARZĄDZANIE STANEM
# ==========================================
if "aktualna_zakladka" not in st.session_state:
    st.session_state.aktualna_zakladka = TAB_OMNIE

if "wybrany_program" not in st.session_state:
    st.session_state.wybrany_program = TAB_KLIMAT

def ustaw_omnie():
    st.session_state.aktualna_zakladka = TAB_OMNIE

def ustaw_program():
    st.session_state.aktualna_zakladka = st.session_state.wybrany_program

def przejdz_do_programu(id_programu):
    st.session_state.aktualna_zakladka = id_programu
    st.session_state.wybrany_program = id_programu

# ==========================================
# NAWIGACJA BOCZNA
# ==========================================
st.sidebar.title("Menu Główne")

st.sidebar.button("O mnie", on_click=ustaw_omnie, use_container_width=True)

with st.sidebar.expander("Programy i Kalkulatory", expanded=True):
    st.radio(
        "Wybierz projekt:",
        options=list(PROGRAMY_DICT.keys()),
        format_func=lambda x: PROGRAMY_DICT[x],
        key="wybrany_program",
        on_change=ustaw_program
    )

st.sidebar.divider()
st.sidebar.markdown("**Kontakt:**\n\n📧 damian.kubiak.projekt@gmail.com\n\n📞 536 481 375")

# ==========================================
# ROUTING I RENDEROWANIE ZAKŁADEK
# ==========================================
if st.session_state.aktualna_zakladka == TAB_OMNIE:
    
    if tlo_url is None:
        st.error(f"🛑 UWAGA: Nie znaleziono pliku '{NAZWA_PLIKU}' w folderze z projektem!")
    else:
        st.markdown(f"""
        <style>
        .stApp {{
            background-image:
                linear-gradient(rgba(247,245,239,.82), rgba(238,234,225,.94)),
                url('{tlo_url}');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
        """, unsafe_allow_html=True)

        st.markdown(
            '<div style="max-width:1100px; margin:35px auto 30px auto;">'
            '<div class="project-kicker">PORTFOLIO · 2026</div>'
            '<h1 style="font-size:clamp(3.2rem, 7vw, 6.5rem); line-height:.88; margin:0; max-width:900px; letter-spacing:-.065em;">DAMIAN<br>KUBIAK</h1>'
            '<p style="margin-top: 25px; font-size: 1.22rem; color: #444; line-height: 1.65;">Budownictwo · konstrukcje · geotechnika · <b>automatyzacja obliczeń inżynierskich</b></p>'
            '</div>', 
            unsafe_allow_html=True
        )

        st.write("")

        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown("""
            <div class="metric-card">
                <div class="metric-label">Edukacja</div>
                <div class="metric-value">ZUT · Budownictwo · IV rok</div>
            </div>
            """, unsafe_allow_html=True)
        with c2:
            st.markdown("""
            <div class="metric-card">
                <div class="metric-label">Specjalność</div>
                <div class="metric-value">Konstrukcje budowlane</div>
            </div>
            """, unsafe_allow_html=True)
        with c3:
            st.markdown("""
            <div class="metric-card">
                <div class="metric-label">Profil</div>
                <div class="metric-value">Inżynieria + Python</div>
            </div>
            """, unsafe_allow_html=True)

        st.write("")
        st.markdown("""
        <div class="portfolio-card">
            <div class="project-kicker">O MNIE</div>
            <div style="font-size:1.08rem; line-height:1.8; max-width:900px;">
                Tworzę narzędzia wspierające obliczenia i analizę problemów
                inżynierskich w budownictwie. Łączę wiedzę z zakresu konstrukcji
                i geotechniki z programowaniem, automatyzacją obliczeń,
                wizualizacją danych oraz generowaniem raportów.
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.write("")
        st.markdown('<div class="project-kicker">PRZYKŁADOWE PROJEKTY</div>', unsafe_allow_html=True)

        p1, p2 = st.columns(2)
        with p1:
            st.markdown("""
            <div class="portfolio-card">
                <div class="project-kicker">01 · KLIMATYCZNE</div>
                <div class="project-title">Generator Obciążeń Klimatycznych</div>
                <div class="project-description">
                    Automatyzacja obliczeń obciążeń wiatrem i śniegiem
                    wraz z wizualizacją stref aerodynamicznych.
                </div>
            </div>
            """, unsafe_allow_html=True)
            st.button("Zobacz projekt ➔", key="btn_klimat", on_click=przejdz_do_programu, args=(TAB_KLIMAT,), use_container_width=True)

        with p2:
            st.markdown("""
            <div class="portfolio-card">
                <div class="project-kicker">02 · GEOTECHNIKA</div>
                <div class="project-title">Posadowienie Pośrednie Zbiornika</div>
                <div class="project-description">
                    Analiza UPL, GEO i SGU, dobór pali, optymalizacja układu
                    oraz moduł kosztorysowy.
                </div>
            </div>
            """, unsafe_allow_html=True)
            st.button("Zobacz projekt ➔", key="btn_zbiornik", on_click=przejdz_do_programu, args=(TAB_ZBIORNIK,), use_container_width=True)

        st.write("")
        st.write("")

        p3, p4 = st.columns(2)
        with p3:
            st.markdown("""
            <div class="portfolio-card">
                <div class="project-kicker">03 · CPTU</div>
                <div class="project-title">Analiza Sondowań CPTU</div>
                <div class="project-description">
                    Przetwarzanie danych pomiarowych, filtracja sygnału
                    i klasyfikacja gruntów metodą SBT Robertson.
                </div>
            </div>
            """, unsafe_allow_html=True)
            st.button("Zobacz projekt ➔", key="btn_cptu", on_click=przejdz_do_programu, args=(TAB_CPTU,), use_container_width=True)

        with p4:
            st.markdown("""
            <div class="portfolio-card" style="height: 94%;">
                <div class="project-kicker">STACK</div>
                <div class="project-title">Python · Streamlit · Plotly</div>
                <div class="project-description">
                    Narzędzia projektowane z myślą o automatyzacji,
                    czytelnej prezentacji wyników i dalszej rozbudowie.
                </div>
            </div>
            """, unsafe_allow_html=True)

elif st.session_state.aktualna_zakladka == TAB_KLIMAT:
    st.title("Generator Obciążeń Klimatycznych")
    st.caption("Eurokod 1 · wiatr · śnieg · wizualizacja · raport")
    
    tab_opis, tab_instrukcja, tab_link = st.tabs(["Opis Programu", "Instrukcja Obsługi", "Uruchom Aplikację"])
    
    with tab_opis:
        st.subheader("Funkcje i algorytmy obliczeniowe")
        st.markdown("""
        Program wyznacza wartości obciążeń klimatycznych dla budynków o rzucie prostokątnym. Algorytmy bazują na poniższych normach wraz z polskimi załącznikami krajowymi:
        
        **Wiatr (PN-EN 1991-1-4:2008/NA:2010):**
        * Wyznaczanie ciśnienia szczytowego ($q_p$) na podstawie mapy stref i kategorii szorstkości terenu.
        * Obliczanie współczynników ciśnienia zewnętrznego ($C_{pe}$) i wewnętrznego ($C_{pi}$).
        * Dynamiczna, wektorowa wizualizacja rozkładu stref aerodynamicznych na dachu na podstawie kierunku wiatru (biblioteka Plotly).
        
        **Śnieg (PN-EN 1991-1-3:2005/NA:2010):**
        * Wyznaczanie wartości charakterystycznej na gruncie ($s_k$) ze wzorów na wysokość n.p.m.
        * Uwzględnianie współczynników kształtu ($μ_1$, $μ_2$), ekspozycji ($C_e$) i termicznego ($C_t$).
        * Generowanie schematów asymetrycznych oraz obliczanie zjawisk krawędziowych (nawisy okapowe, parcie na płotki, zaspy przy attykach).
        
        **Wyniki wyjściowe:**
        * Bezpośrednie zestawienie sił (wartości netto na m²) dla poszczególnych stref ścian i dachu.
        * Raport tekstowy gotowy do eksportu.
        """)
        
        st.divider()
        if os.path.exists("screen_wiatr.png"):
            st.image("screen_wiatr.png", caption="Wizualizacja stref obciążeń na dachu", use_container_width=True)
        
    with tab_instrukcja:
        st.subheader("Instrukcja obsługi")
        st.markdown("""
        1. **Geometria budynku:** W lewym panelu podaj wymiary gabarytowe: szerokość ($b$), długość ($d$), wysokość ($h$) oraz wybierz typ i nachylenie dachu.
        2. **Lokalizacja i teren:** Określ strefy klimatyczne, wysokość nad poziomem morza oraz właściwą kategorię terenu.
        3. **Parametry dodatkowe:** Skonfiguruj ewentualną attykę, płotki przeciwśniegowe i zdefiniuj współczynnik ciśnienia wewnętrznego ($C_{pi}$).
        4. **Wizualizacja (Wiatr):** Przełączając główny sterownik kierunku wiatru na górze ekranu (0° lub 90°), wygeneruj układ stref aerodynamicznych na rzucie dachu.
        5. **Raport:** W ostatniej zakładce możesz pobrać plik `.txt`. Zestawione w nim wartości sił mogą posłużyć jako dane wejściowe do dalszego projektowania.
        """)
        
    with tab_link:
        st.info("Aplikacja udostępniona w chmurze.")
        st.link_button("Otwórz Generator Obciążeń Klimatycznych ➔", "https://generator-klimatyczne.streamlit.app/")

elif st.session_state.aktualna_zakladka == TAB_ZBIORNIK:
    st.title("Posadowienie Pośrednie Zbiornika")
    st.caption("UPL · GEO · SGU · pale · optymalizacja · kosztorys")
    
    tab_opis, tab_instrukcja, tab_link = st.tabs(["Opis Programu", "Instrukcja Obsługi", "Uruchom Aplikację"])
    
    with tab_opis:
        st.subheader("Funkcje i algorytmy obliczeniowe")
        st.markdown("""
        Zaawansowany system inżynierski przeznaczony do kompleksowego projektowania i optymalizacji głębokiego posadowienia podziemnych zbiorników retencyjnych w trudnych warunkach gruntowych.
        
        **Kluczowe moduły i funkcjonalności:**
        * **Analiza Stanów Granicznych:** Weryfikacja nośności i stateczności w stanach **UPL** (utrata stateczności ogólnej/wypór wodny), **GEO** (nośność podłoża i pali) oraz **SGU**.
        * **Projektowanie Żelbetu i Zbrojenia:** Dobór średnic prętów podłużnych i weryfikacja nośności przekrojów pali.
        * **Moduł Kosztorysowy:** Automatyczna wycena materiałów i robocizny.
        * **Moduł Optymalizacji Rozkładu Posadowienia:** Automatyczne testowanie kombinacji siatek pali przy zachowaniu normowych odstępów ($3D$) oraz ograniczeń skrajni palownicy.
        * **Generator Raportów Obliczeniowych:** Tworzenie szczegółowych not obliczeniowych z rozpisaniem wzorów normowych (dokumentacja inżynierska ZUT).
        """)
        
        st.divider()
        if os.path.exists("screen_zbiornik.png"):
            st.image("screen_zbiornik.png", caption="Raport obliczeniowy i wyniki optymalizacji siatki pali", use_container_width=True)
        
    with tab_instrukcja:
        st.subheader("Instrukcja wprowadzania danych (Panel Boczny)")
        st.markdown("""
        Szczegółowy opis konfiguracji parametrów w lewym panelu bocznym aplikacji:
        
        **1. Parametry geometryczne zbiornika**  
        Wprowadź zewnętrzne gabaryty, grubość ścian i dna oraz ciężar objętościowy betonu konstrukcyjnego.
        
        **2. Zagłębienie i Naziom**  
        Zdefiniuj grubość warstwy gruntu nad stropem oraz ciężar objętościowy naziomu.
        
        **3. Profil Geotechniczny**  
        Wybierz metodę definiowania parametrów gruntu (automatyczna korelacja $I_D$ / $I_L$ lub ręczne wprowadzanie oporów pobocznicy) i zdefiniuj warstwowanie.
        
        **4. Warunki Hydrogeologiczne**  
        Określ poziom wody gruntowej na zewnątrz (kluczowe dla stanu UPL – woda wywołuje wypór pustego zbiornika).
        
        **5. Parametry Pali**  
        Wprowadź średnicę pala $D$, długość, planowaną liczbę sztuk oraz technologię wykonania.
        
        **6. Ograniczenia Wykonawcze i Koszty**  
        Ustaw parametry placu budowy oraz aktualne stawki rynkowe do wyceny kosztorysowej.
        """)
        
    with tab_link:
        st.info("Narzędzie wdrożone w środowisku chmurowym.")
        st.link_button("Otwórz Kalkulator Posadowienia ➔", "https://posadowienie-posrednie-zbiornika.streamlit.app/")

elif st.session_state.aktualna_zakladka == TAB_CPTU:
    st.title("Analiza sondowań CPTU")
    st.caption("CPTU · filtracja danych · SBT Robertson · litologia")
    
    tab_opis, tab_instrukcja, tab_link = st.tabs(["Opis Programu", "Instrukcja Obsługi", "Uruchom Aplikację"])
    
    with tab_opis:
        st.subheader("Funkcje i algorytmy obliczeniowe")
        st.markdown("""
        Program do automatycznej ekstrakcji i interpretacji surowych danych geotechnicznych z sondowań statycznych CPTU. 
        
        **Kluczowe możliwości algorytmu:**
        * **Filtracja sygnału:** Cyfrowe wygładzanie danych (algorytm średniej ruchomej) w celu eliminacji szumów.
        * **Ekstrakcja parametrów:** Wyznaczanie rzeczywistych oporów stożka ($q_c$), tarcia na tulei ($f_s$), wskaźnika tarcia ($R_f$) oraz ciśnienia porowego ($u_2$).
        * **Klasyfikacja SBT Robertsona:** Obliczanie bezwymiarowego wskaźnika zachowania gruntu ($I_c$).
        * **Zestawienia statystyczne:** Generowanie czytelnych, graficznych profilów głębokościowych z kolorową identyfikacją warstw oraz obliczanie procentowego udziału miąższości.
        """)
        
        st.divider()
        if os.path.exists("screen_cptu.png"):
            st.image("screen_cptu.png", caption="Kolorowy profil litologiczny SBT z wygładzaniem szumów", use_container_width=True)
        
    with tab_instrukcja:
        st.subheader("Instrukcja obsługi")
        st.markdown("""
        **1. Źródło danych (Import pliku)**  
        W lewym panelu bocznym przeciągnij i upuść surowy plik z sondy (w formacie `.txt` lub `.csv`). Aplikacja wymaga standardowych tagów geotechnicznych: `D=` (głębokość), `QC=` (opór stożka) oraz `FS=` (tarcie).
        
        **2. Cyfrowa Filtracja Sygnału**  
        Za pomocą suwaka "Okno uśredniania" modyfikujesz interwał algorytmu średniej ruchomej, co pozwala uzyskać spójny i czytelny wykres profilu, eliminując szumy z aparatury.
        
        **3. Interpretacja Wyników**  
        * **Profil CPTU i Litologia:** Osie prezentujące wykresy oporu stożka, tarcia, ciśnienia porowego oraz wygenerowany blok wydzieleń gruntowych.
        * **Zestawienie Gruntów:** Tabelaryczny, sumaryczny udział objętościowy poszczególnych rodzajów gruntu.
        """)
        
    with tab_link:
        st.info("Aplikacja wdrożona w środowisku chmurowym.")
        st.link_button("Otwórz program do analizy CPTU ➔", "https://badanie-cptu.streamlit.app/")

else:
    st.error("Błąd nawigacji.")
    st.button("Wróć do strony głównej", on_click=ustaw_omnie)
