import zipfile
import xml.etree.ElementTree as ET
import sys
import traceback

def extract_text(docx_path, out_path):
    try:
        with zipfile.ZipFile(docx_path) as z:
            xml_content = z.read('word/document.xml')
        
        tree = ET.fromstring(xml_content)
        texts = []
        # Find all text nodes
        for elem in tree.iter():
            if elem.tag.endswith('t') and elem.text:
                texts.append(elem.text)
        
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(texts))
    except Exception as e:
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(f"Error: {str(e)}\n\n")
            f.write(traceback.format_exc())

if __name__ == '__main__':
    extract_text(sys.argv[1], sys.argv[2])
