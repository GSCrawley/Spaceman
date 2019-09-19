from spaceman import is_word_guessed, is_guess_in_word, get_guessed_word

def test_is_word_guessed():
    assert is_word_guessed(('breast'),['b','r','e','a','s','t']) is True
    assert is_word_guessed(('eggs'),['e','g','g','s']) is True
    assert is_word_guessed(('butter'),['b','u','t','t','e','r']) is True

def test_is_guess_in_word():
    assert is_guess_in_word(('a'), ('apple')) is True
    assert is_guess_in_word(('b'), ('banana')) is True
    assert is_guess_in_word(('c'), ('carrot')) is True

def test_get_guessed_word():
    assert get_guessed_word(('table'), ['t','a','b','l']) == " t a b l  _ " 
    assert get_guessed_word(('chair'), ['c','h','a','r']) == " c h a  _ r "
    assert get_guessed_word(('carpet'), ['c','a','p','e','t']) == " c a  _ p e t "
