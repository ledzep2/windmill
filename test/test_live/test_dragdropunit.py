# Generated by the windmill services transformer
from windmill.authoring import WindmillTestClient

def test_dragdropunit():
    client = WindmillTestClient(__name__)

    assert client.open(url=u'http://windmill.osafoundation.org/windmill-unittests/jqueryui152/demos/functional/index.html')
    assert client.waits.forPageLoad(timeout=u'40000')
    #test the draggable widgets
    assert client.click(link=u'Draggable')
    assert client.dragDropElem(pixels=u'(200,0)', id=u'dragImage')
    assert client.waits.sleep(milliseconds=u'500')
    assert client.scroll(coords=u'(0,550)')
    assert client.waits.sleep(milliseconds=u'500')
    assert client.dragDropElem(pixels=u'(300,0)', id=u'divDrag')
    #assert client.asserts.assertProperty(validator=u'style.left|289px', id=u'divDrag')
    assert client.dragDropElem(xpath=u'/html/body/div/div[2]/div/div[2]/form/div[2]/table/tbody/tr/td[2]/div/div[3]/div[3]/div/div', pixels=u'(257,0)')
    #assert client.asserts.assertProperty(validator=u'style.left|246px', id=u'draggable-handle-div')
    assert client.dragDropElem(link=u'Drag me', pixels=u'(420,0)')
    #assert client.asserts.assertProperty(validator=u'style.left|409px', id=u'draggable-dragPrevention')
    #test the droppable widgets
    assert client.click(link=u'Droppable')
    assert client.click(link=u'Droppable')
    assert client.waits.sleep(milliseconds=u'500')
    #assert client.waits.forPageLoad(timeout=u'20000')
    assert client.dragDropElem(xpath=u'/html/body/div/div[2]/div/div[2]/form/div[2]/table/tbody/tr/td[2]/div/div/div[3]/div/ul/li[2]/img', pixels=u'(310,0)')
    assert client.waits.sleep(milliseconds=u'800')
    assert client.asserts.assertProperty(xpath=u'/html/body/div/div[2]/div/div[2]/form/div[2]/table/tbody/tr/td[2]/div/div/div[3]/div/div/img', validator=u'src|templates/images/P1010039.JPG')
    assert client.dragDropElemToElem(xpath=u'/html/body/div/div/div/div[2]/form/div[2]/table/tbody/tr[1]/td[2]/div/div/div[3]/div/ul/li/img', optxpath=u'/html/body/div/div/div/div[2]/form/div[2]/table/tbody/tr[1]/td[2]/div/div/div[3]/div/div')    
    assert client.waits.sleep(milliseconds=u'500')
    assert client.asserts.assertProperty(xpath=u"/html/body/div/div[2]/div/div[2]/form/div[2]/table/tbody/tr/td[2]/div/div/div[3]/div/div/img", validator=u'src|P1010020.JPG')
    assert client.scroll(coords=u'(0,500)')
    assert client.dragDropElemToElem(xpath=u"/html/body/div/div[2]/div/div[2]/form/div[2]/table/tbody/tr/td[2]/div/div[2]/div[3]/div", optxpath=u"/html/body/div/div[2]/div/div[2]/form/div[2]/table/tbody/tr/td[2]/div/div[2]/div[3]/div[4]")
    assert client.waits.sleep(milliseconds=u'500')
    assert client.dragDropElemToElem(xpath=u"/html/body/div/div[2]/div/div[2]/form/div[2]/table/tbody/tr/td[2]/div/div[2]/div[3]/div[2]", optxpath=u"/html/body/div/div[2]/div/div[2]/form/div[2]/table/tbody/tr/td[2]/div/div[2]/div[3]/div[4]")
    assert client.waits.sleep(milliseconds=u'500')
    assert client.dragDropElem(xpath=u'/html/body/div/div[2]/div/div[2]/form/div[2]/table/tbody/tr/td[2]/div/div[2]/div[3]/div', pixels=u'(0,250)')
    assert client.waits.sleep(milliseconds=u'500')
    assert client.asserts.assertText(xpath=u'/html/body/div/div[2]/div/div[2]/form/div[2]/table/tbody/tr/td[2]/div/div[2]/div[3]/div[4]', validator=u'Dropped!')
    assert client.dragDropElem(xpath=u'/html/body/div/div[2]/div/div[2]/form/div[2]/table/tbody/tr/td[2]/div/div[2]/div[3]/div[2]', pixels=u'(0,200)')
    assert client.waits.sleep(milliseconds=u'500')
    assert client.asserts.assertText(xpath=u'/html/body/div/div[2]/div/div[2]/form/div[2]/table/tbody/tr/td[2]/div/div[2]/div[3]/div[4]', validator=u'Dropped! Dropped!')
    #test the sortable widgets
    assert client.click(link=u'Sortable')
    assert client.click(link=u'Sortable')
    assert client.waits.sleep(milliseconds=u'500')
    #assert client.waits.forPageLoad(timeout=u'20000')
    assert client.asserts.assertJS(js=u"_w.document.getElementById('user_Susan').parentNode.childNodes.length == 11;")
    assert client.dragDropElem(pixels=u'(160,0)', id=u'user_Susan')
    assert client.asserts.assertJS(js=u"_w.document.getElementById('user_Susan').parentNode.childNodes.length == 12;")
    #test the dialog widgets
    assert client.click(link=u'Dialog')
    assert client.click(link=u'Dialog')
    #assert client.waits.forPageLoad(timeout=u'20000')
    assert client.dragDropElem(xpath=u"/html/body[@id='functional_demos']/div[3]/div[1]/div[1]", pixels=u'(150,0)')
    #assert client.asserts.assertProperty(xpath=u'/html/body/div[3]', validator=u'style.left|455px')
    #test the slider widgets
    assert client.click(link=u'Slider')
    assert client.click(link=u'Slider')
    assert client.waits.sleep(milliseconds=u'500')
    #assert client.waits.forPageLoad(timeout=u'20000')
    assert client.dragDropElem(xpath=u'/html/body/div/div[2]/div/div[2]/form/div[2]/table/tbody/tr/td[2]/div/div/div[3]/div/a/div', pixels=u'(80,0)')
    #Assert client.asserts.assertProperty(xpath=u'/html/body/div/div[2]/div/div[2]/form/div[2]/table/tbody/tr/td[2]/div/div/div[3]/div/a/div', validator=u'style.left|79px')
    assert client.dragDropElem(xpath=u'/html/body/div/div[2]/div/div[2]/form/div[2]/table/tbody/tr/td[2]/div/div[2]/div[3]/div/a/div', pixels=u'(50,0)')
    assert client.waits.sleep(milliseconds=u'500')
    assert client.dragDropElem(xpath=u'/html/body/div/div[2]/div/div[2]/form/div[2]/table/tbody/tr/td[2]/div/div[2]/div[3]/div/a[2]/div', pixels=u'(-20,0)')
    #assert client.asserts.assertProperty(xpath=u'/html/body/div/div[2]/div/div[2]/form/div[2]/table/tbody/tr/td[2]/div/div[2]/div[3]/div/a/div', validator=u'style.left|49px')
    #assert client.asserts.assertProperty(xpath=u'/html/body/div/div[2]/div/div[2]/form/div[2]/table/tbody/tr/td[2]/div/div[2]/div[3]/div/a[2]/div', validator=u'style.left|81px')
    assert client.click(link=u'Draggable')