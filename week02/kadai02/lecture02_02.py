import xml.etree.ElementTree as ET

def lecture02_02() -> None:
    # ルート要素bookの作成
    root = ET.Element('book')
    
    # article要素の作成
    article = ET.SubElement(root, 'article')
    article.set('title', '卒業論文')
    
    # articleのchapter要素を作成
    chapter1 = ET.SubElement(article, 'chapter')
    chapter1.set('id', '1')
    chapter1.set('name', 'はじめに')
    chapter1.set('pages', '2')
    
    chapter2 = ET.SubElement(article, 'chapter')
    chapter2.set('id', '2')
    chapter2.set('name', '基礎理論')
    chapter2.set('pages', '8')
    
    chapter3 = ET.SubElement(article, 'chapter')
    chapter3.set('id', '3')
    chapter3.set('name', '実験方法')
    chapter3.set('pages', '6')
    
    chapter4 = ET.SubElement(article, 'chapter')
    chapter4.set('id', '4')
    chapter4.set('name', '結果と考察')
    chapter4.set('pages', '2')
    
    chapter5 = ET.SubElement(article, 'chapter')
    chapter5.set('id', '5')
    chapter5.set('name', 'まとめ')
    chapter5.set('pages', '1')
    
    chapter6 = ET.SubElement(article, 'chapter')
    chapter6.set('id', '6')
    chapter6.set('name', '参考文献')
    chapter6.set('pages', '2')
    
    # novel要素の作成
    novel = ET.SubElement(root, 'novel')
    
    # novelのchapter要素を作成
    novel_chapter1 = ET.SubElement(novel, 'chapter')
    novel_chapter1.set('id', '1')
    novel_chapter1.set('name', '1日のはじまり')
    novel_chapter1.set('pages', '2')
    
    novel_chapter2 = ET.SubElement(novel, 'chapter')
    novel_chapter2.set('id', '2')
    novel_chapter2.set('name', '朝食')
    novel_chapter2.set('pages', '8')
    
    novel_chapter3 = ET.SubElement(novel, 'chapter')
    novel_chapter3.set('id', '3')
    novel_chapter3.set('name', '仕事')
    novel_chapter3.set('pages', '6')
    
    novel_chapter4 = ET.SubElement(novel, 'chapter')
    novel_chapter4.set('id', '4')
    novel_chapter4.set('name', '帰宅後')
    novel_chapter4.set('pages', '2')
    
    novel_chapter5 = ET.SubElement(novel, 'chapter')
    novel_chapter5.set('id', '5')
    novel_chapter5.set('name', '新しい朝')
    novel_chapter5.set('pages', '1')
    
    # ツリーの作成とファイルへの書き出し
    with open('lecture02_02_data.xml', 'wb') as f:
        import xml.dom.minidom as md
        f.write(md.parseString(ET.tostring(root, encoding='utf-8', xml_declaration=True)).toprettyxml(indent='  ',encoding="utf-8"))

if __name__ == '__main__':
    lecture02_02()
