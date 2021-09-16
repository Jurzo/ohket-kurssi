import postinumerot

mockData = {
    "74701": "KIURUVESI",
    "35540": "JUUPAJOKI",
    "74700": "KIURUVESI",
    "73460": "MUURUVESI",
    "43800": "KIVIJÄRVI",
    "91150": "YLI-OLHAVA",
    "65374": "SMART POST"
}

def test_data_flip():
    flipped_data = postinumerot.flipData(mockData)
    assert len(flipped_data) == 6
    assert len(flipped_data.get('KIURUVESI')) == 2

def test_mockattu_data_monta_numeroa(mocker):
    mocker.patch('postidata.getData', return_value = mockData)
    vastaus = postinumerot.haePostitoimipaikanNumerot('kiuruvesi')

    assert len(vastaus) > 1

def test_mockattu_data_yksi_numero(mocker):
    mocker.patch('postidata.getData', return_value = mockData)
    vastaus = postinumerot.haePostitoimipaikanNumerot('kivijärvi')

    assert len(vastaus) == 1

def test_mockattu_data_ei_tulosta(mocker):
    mocker.patch('postidata.getData', return_value = mockData)
    vastaus = postinumerot.haePostitoimipaikanNumerot('asd')

    assert "Virheellinen" in vastaus

def test_oikea_data_yksi_numero():
    vastaus = postinumerot.haePostitoimipaikanNumerot('siuntio')
    assert len(vastaus) == 1

def test_oikea_data_monta_numeroa():
    vastaus = postinumerot.haePostitoimipaikanNumerot('helsinki')
    assert len(vastaus) > 1

def test_kirjoitusasu_ei_vaikuta_tulokseen():
    vastaus1 = postinumerot.haePostitoimipaikanNumerot('smartpost')
    vastaus2 = postinumerot.haePostitoimipaikanNumerot('smart post')

    assert vastaus1 == vastaus2

def test_kirjoitusasu_ei_vaikuta_tulokseen_mock_data(mocker):
    mocker.patch('postidata.getData', return_value = mockData)
    vastaus1 = postinumerot.haePostitoimipaikanNumerot('smartpost')
    vastaus2 = postinumerot.haePostitoimipaikanNumerot('smart post')

    assert vastaus1 == vastaus2