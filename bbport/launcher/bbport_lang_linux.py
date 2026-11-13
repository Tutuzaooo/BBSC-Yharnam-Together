# SPDX-License-Identifier: GPL-2.0-or-later
"""Launcher texts shown only on Linux (the port built from source or packaged there), in every launcher
language (see bbport_lang.py). Russian comes from the texts next to the English in bbport_launcher_win.py."""

LINUX_KEYS = [
    'DLSS needs {} in {}: {} missing (build.sh copies them when DLSS_SDK_ROOT is set). Until then FSR 3.1 is used.',
    'DLSS uses {} in {} (✓ found). On other GPUs FSR 3.1 is used.',
    "Auto (Steam Deck grid at 1280 × 800, else the game's own)",
    "The game's own",
    'Light grid',
    "The grid the game sorts its lights into (community Light Grid patches). A smaller one is faster; match it to the output. Auto: the Steam Deck's 1280 × 800 grid at that output, the game's own grid at any other. Set at start: after changing the output in the game, restart it. Lights missing or cut off near the screen's edges: choose the game's own.",
]

LINUX = {
    'ar': [
        'يحتاج DLSS إلى {} في {}: الناقص {} (ينسخها build.sh عند تعيين DLSS_SDK_ROOT). حتى ذلك الحين يُستخدم FSR 3.1.',
        'يستخدم DLSS الملفات {} في {} (✓ موجودة). على المعالجات الرسومية الأخرى يُستخدم FSR 3.1.',
        'تلقائي (شبكة Steam Deck عند 1280 × 800، وإلا شبكة اللعبة الأصلية)',
        'شبكة اللعبة الأصلية',
        'شبكة الإضاءة',
        'الشبكة التي توزّع اللعبة مصادر الضوء عليها (رقع Light Grid من المجتمع). الشبكة الأصغر أسرع؛ اجعلها مطابقة لدقة الإخراج. تلقائي: شبكة Steam Deck بدقة 1280 × 800 عند هذا الإخراج، وشبكة اللعبة الأصلية عند أي إخراج آخر. تُضبط عند التشغيل: بعد تغيير الإخراج داخل اللعبة أعد تشغيلها. إذا اختفت الأضواء أو قُطعت قرب حواف الشاشة فاختر شبكة اللعبة الأصلية.',
    ],
    'es': [
        'DLSS necesita {} en {}: faltan {} (build.sh los copia cuando DLSS_SDK_ROOT está definido). Mientras tanto se usa FSR 3.1.',
        'DLSS usa {} en {} (✓ encontrados). En otras GPU se usa FSR 3.1.',
        'Automático (rejilla de Steam Deck a 1280 × 800; si no, la del juego)',
        'La del juego',
        'Rejilla de luces',
        'La rejilla en la que el juego ordena sus luces (parches Light Grid de la comunidad). Una más pequeña es más rápida; ajústala a la salida. Automático: la rejilla de 1280 × 800 de Steam Deck con esa salida, la del juego con cualquier otra. Se fija al iniciar: tras cambiar la salida en el juego, reinícialo. Si faltan luces o se cortan cerca de los bordes de la pantalla, elige la del juego.',
    ],
    'pt': [
        'O DLSS precisa de {} em {}: faltam {} (o build.sh os copia quando DLSS_SDK_ROOT está definido). Até lá, o FSR 3.1 é usado.',
        'O DLSS usa {} em {} (✓ encontrados). Em outras GPUs, o FSR 3.1 é usado.',
        'Automático (grade do Steam Deck em 1280 × 800; senão, a do jogo)',
        'A do jogo',
        'Grade de luzes',
        'A grade em que o jogo organiza suas luzes (patches Light Grid da comunidade). Uma menor é mais rápida; combine-a com a saída. Automático: a grade de 1280 × 800 do Steam Deck nessa saída, a do jogo em qualquer outra. Definida ao iniciar: depois de mudar a saída no jogo, reinicie-o. Se faltarem luzes ou elas forem cortadas perto das bordas da tela, escolha a do jogo.',
    ],
    'fr': [
        'DLSS a besoin de {} dans {} : {} manquant(s) (build.sh les copie quand DLSS_SDK_ROOT est défini). En attendant, FSR 3.1 est utilisé.',
        'DLSS utilise {} dans {} (✓ trouvés). Sur les autres GPU, FSR 3.1 est utilisé.',
        'Auto (grille du Steam Deck en 1280 × 800, sinon celle du jeu)',
        'Celle du jeu',
        'Grille de lumières',
        "La grille dans laquelle le jeu range ses lumières (correctifs Light Grid de la communauté). Une grille plus petite est plus rapide ; accordez-la à la sortie. Auto : la grille 1280 × 800 du Steam Deck à cette sortie, celle du jeu à toute autre. Fixée au démarrage : après avoir changé la sortie dans le jeu, redémarrez-le. Si des lumières manquent ou sont coupées près des bords de l'écran, choisissez celle du jeu.",
    ],
    'de': [
        'DLSS braucht {} in {}: {} fehlen (build.sh kopiert sie, wenn DLSS_SDK_ROOT gesetzt ist). Bis dahin wird FSR 3.1 verwendet.',
        'DLSS nutzt {} in {} (✓ gefunden). Auf anderen GPUs wird FSR 3.1 verwendet.',
        'Auto (Steam-Deck-Raster bei 1280 × 800, sonst das des Spiels)',
        'Das des Spiels',
        'Lichtraster',
        'Das Raster, in das das Spiel seine Lichter einsortiert (Light-Grid-Patches der Community). Ein kleineres ist schneller; passe es an die Ausgabe an. Auto: das 1280 × 800-Raster des Steam Decks bei dieser Ausgabe, das Raster des Spiels bei jeder anderen. Wird beim Start gesetzt: Nach einem Wechsel der Ausgabe im Spiel das Spiel neu starten. Fehlen Lichter oder sind sie an den Bildschirmrändern abgeschnitten, wähle das des Spiels.',
    ],
    'it': [
        'DLSS richiede {} in {}: mancano {} (build.sh li copia quando DLSS_SDK_ROOT è impostato). Nel frattempo si usa FSR 3.1.',
        'DLSS usa {} in {} (✓ trovati). Sulle altre GPU si usa FSR 3.1.',
        'Automatico (griglia di Steam Deck a 1280 × 800, altrimenti quella del gioco)',
        'Quella del gioco',
        'Griglia delle luci',
        "La griglia in cui il gioco ordina le sue luci (patch Light Grid della comunità). Una più piccola è più veloce; abbinala all'uscita. Automatico: la griglia 1280 × 800 di Steam Deck con quell'uscita, quella del gioco con qualsiasi altra. Impostata all'avvio: dopo aver cambiato l'uscita nel gioco, riavvialo. Se mancano luci o sono tagliate vicino ai bordi dello schermo, scegli quella del gioco.",
    ],
    'pl': [
        'DLSS potrzebuje {} w {}: brakuje {} (build.sh kopiuje je, gdy ustawiono DLSS_SDK_ROOT). Do tego czasu używany jest FSR 3.1.',
        'DLSS używa {} w {} (✓ znalezione). Na innych GPU używany jest FSR 3.1.',
        'Automatycznie (siatka Steam Decka przy 1280 × 800, w innym razie siatka gry)',
        'Siatka gry',
        'Siatka świateł',
        'Siatka, w którą gra układa swoje światła (społecznościowe łatki Light Grid). Mniejsza jest szybsza; dopasuj ją do wyjścia. Automatycznie: siatka Steam Decka 1280 × 800 przy takim wyjściu, siatka gry przy każdym innym. Ustawiana przy starcie: po zmianie wyjścia w grze uruchom ją ponownie. Jeśli świateł brakuje albo są ucięte przy krawędziach ekranu, wybierz siatkę gry.',
    ],
    'tr': [
        'DLSS için {} dosyaları {} içinde gerekli: {} eksik (DLSS_SDK_ROOT ayarlıysa build.sh onları kopyalar). O zamana kadar FSR 3.1 kullanılır.',
        'DLSS, {} dosyalarını {} içinde kullanır (✓ bulundu). Diğer GPU’larda FSR 3.1 kullanılır.',
        "Otomatik (1280 × 800'de Steam Deck ızgarası, değilse oyunun kendi ızgarası)",
        'Oyunun kendi ızgarası',
        'Işık ızgarası',
        "Oyunun ışıklarını yerleştirdiği ızgara (topluluğun Light Grid yamaları). Küçük olanı daha hızlıdır; çıkışa uygun olanı seçin. Otomatik: bu çıkışta Steam Deck'in 1280 × 800 ızgarası, diğer her çıkışta oyunun kendi ızgarası. Başlangıçta ayarlanır: oyunda çıkışı değiştirdikten sonra oyunu yeniden başlatın. Ekran kenarlarında ışıklar eksikse ya da kesiliyorsa oyunun kendi ızgarasını seçin.",
    ],
    'zh': [
        'DLSS 需要 {}（位于 {}）：缺少 {}（设置了 DLSS_SDK_ROOT 时，build.sh 会复制它们）。在此之前使用 FSR 3.1。',
        'DLSS 使用 {}（位于 {}，✓ 已找到）。其他显卡使用 FSR 3.1。',
        '自动（1280 × 800 时使用 Steam Deck 网格，否则使用游戏自带网格）',
        '游戏自带',
        '光照网格',
        '游戏用来划分光源的网格（社区的 Light Grid 补丁）。较小的网格更快；请与输出分辨率匹配。自动：输出为 1280 × 800 时使用 Steam Deck 的网格，其他输出使用游戏自带网格。启动时设定：在游戏中更改输出后请重启游戏。如果屏幕边缘附近的光源缺失或被截断，请选择游戏自带网格。',
    ],
    'ja': [
        'DLSS には {} が必要です（場所：{}）：{} が見つかりません（DLSS_SDK_ROOT を設定すると build.sh がコピーします）。それまでは FSR 3.1 を使います。',
        'DLSS は {} を使います（場所：{}、✓ 見つかりました）。ほかの GPU では FSR 3.1 を使います。',
        '自動（1280 × 800 では Steam Deck 用グリッド、それ以外はゲーム本来のもの）',
        'ゲーム本来のもの',
        'ライトグリッド',
        'ゲームがライトを振り分けるグリッドです（コミュニティの Light Grid パッチ）。小さいほど高速です。出力に合わせてください。自動：出力が 1280 × 800 のときは Steam Deck 用のグリッド、それ以外はゲーム本来のグリッドを使います。起動時に決まるため、ゲーム内で出力を変えたらゲームを再起動してください。画面の端でライトが消えたり切れたりする場合は、ゲーム本来のものを選んでください。',
    ],
    'ko': [
        'DLSS에는 {}가 필요합니다(위치: {}): {} 없음(DLSS_SDK_ROOT를 설정하면 build.sh가 복사합니다). 그때까지는 FSR 3.1을 사용합니다.',
        'DLSS는 {}를 사용합니다(위치: {}, ✓ 찾음). 다른 GPU에서는 FSR 3.1을 사용합니다.',
        '자동(1280 × 800에서는 Steam Deck 그리드, 그 외에는 게임 기본 그리드)',
        '게임 기본 그리드',
        '라이트 그리드',
        '게임이 광원을 나누어 담는 그리드입니다(커뮤니티 Light Grid 패치). 작을수록 빠르며, 출력에 맞추세요. 자동: 출력이 1280 × 800이면 Steam Deck용 그리드, 그 외에는 게임 기본 그리드를 씁니다. 시작할 때 정해지므로 게임에서 출력을 바꾼 뒤에는 게임을 다시 시작하세요. 화면 가장자리에서 빛이 사라지거나 잘리면 게임 기본 그리드를 선택하세요.',
    ],
}
