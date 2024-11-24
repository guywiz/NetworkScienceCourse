import xml.etree.ElementTree as ET
from tulip import *

G = tlp.newGraph()
G.setName('SouthernWomen')
G.getStringProperty('type')
nodemap = {}

tree = ET.parse('SouthernWomen.xml')
root = tree.getroot()
for nodeset in root.iter('nodeset'):
    type = nodeset.get('type')
    for node in nodeset.findall('node'):
        n = G.addNode()
        G['type'][n] = type
        G['viewShape'][n] = tlp.NodeShape.Icon
        if type == 'agent':
            G['viewIcon'][n] = 'mdi-face-woman'
        if type == 'event':
            G['viewIcon'][n] = 'mdi-party-popper'
        G['viewLabel'][n] = node.get('id')
        nodemap[G['viewLabel'][n]] = n

for edge in root.iter('edge'):
    source = edge.get('source')
    target = edge.get('target')
    value = int(float(edge.get('value')))
    if value:
        s = nodemap[source]
        t = nodemap[target]
        G.addEdge(s, t)

tlp.saveGraph(G, './SouthernWomen.tlp')


