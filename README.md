# splitCMTXML

This code split the XML file of CMT (http://cmt.research.microsoft.com) for offline reviewing. If the XML contains more than one papers, it divides into multiple XMLs that each XML contains one paper.

Usage: `$python splitCMTXML.py < yourxmlfile.xml`

After filling the reviews, you can concatenate them by mergeCMTXML.py.

Usage: `$cat *.xml | python mergeCMTXML.py > merged.xml`
