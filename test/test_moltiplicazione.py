from ..operazioni import moltiplicazione

def test_moltiplicazione_numeri_interi():
    # 2 * 3 = 6
    assert moltiplicazione(2, 3) == 6
    # -1 * 5 = -5
    assert moltiplicazione(-1, 5) == -5
    # 0 * 0 = 0
    assert moltiplicazione(0, 0) == 0

def test_moltiplicazione_numeri_decimali():
    # 1.5 * 2.0 = 3.0
    assert moltiplicazione(1.5, 2.0) == 3.0
    # -1.0 * 0.5 = -0.5
    assert moltiplicazione(-1.0, 0.5) == -0.5

def test_moltiplicazione_con_stringhe():
    # Assumendo che la funzione restituisca None per tipi non validi
    # come faceva la funzione somma nel tuo esempio
    assert moltiplicazione("hello", 5) is None
    assert moltiplicazione(10, "world") is None
    assert moltiplicazione("a", "b") is None

def test_moltiplicazione_con_zero():
    # Qualsiasi numero moltiplicato per 0 deve dare 0
    assert moltiplicazione(0, 5) == 0
    assert moltiplicazione(100, 0) == 0