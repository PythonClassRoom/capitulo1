def test_string_format():
    cad1 = 'hola'
    cad2 = 'mundo'
    cad_1 = "%s %s" % (cad1, cad2)
    cad_2 = "{0} {1}".format(cad1, cad2)
    assert cad_1 == cad_2
