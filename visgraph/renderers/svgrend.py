
import visgraph.renderers as vg_render

example = '''
<?xml version="1.0" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" 
"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">

<svg width="100%" height="100%" version="1.1"
xmlns="http://www.w3.org/2000/svg">

<rect x="20" y="20" rx="20" ry="20" width="250" height="100"
style="fill:red;stroke:black;stroke-width:5;opacity:0.5"/>
</svg>
'''

class SvgGraphRenderer(vg_render.GraphRenderer):

    def __init__(self, graph, svgfile):
        vg_render.GraphRenderer.__init__(self, graph)
        self.svgfile = svgfile
        self._node_xml = []
        self._edge_xml = []

    def renderNode(self, nid, ninfo, xpos, ypos):
        rectstr = '<rect x="%d" y="%d" width="10" height="10" style="fill:red;stroke:black;stroke-width:5;opacity:0.5"/>' % (xpos,ypos)
        self._node_xml.append(rectstr)

    def renderEdge(self, eid, einfo, points):
        pointstr = ' '.join([ '%d,%d' % (x,y) for x,y in points ])
        edgestr = '<polyline points="%s" style="fill:white;stroke:red;stroke-width:2"/>' % pointstr
        self._edge_xml.append(edgestr)

    def setNodeSizes(self, graph):
        # Do the node sizing...
        for nid,ninfo in graph.getNodes():
            ninfo['size'] = (10,10)

    def beginRender(self, xsize, ysize):
        vg_render.GraphRenderer.beginRender(self, xsize, ysize)

    def endRender(self):
        # Actually write out the file.
        f = file(self.svgfile,'wb')
        f.write('<?xml version="1.0" standalone="no"?>\n')
        #f.write('<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd" >\n')
        xsize = self._vg_canvas_width
        ysize = self._vg_canvas_height
        f.write('<svg width="%d" height="%d" version="1.1" xmlns="http://www.w3.org/2000/svg">\n' % (xsize,ysize))
        for x in self._node_xml:
            f.write(x + '\n')
        for x in self._edge_xml:
            f.write(x + '\n')
        f.write('</svg>\n')
        f.close()

if __name__ == '__main__':

    import visgraph.graphcore as vg_graphcore
    import visgraph.layouts.dynadag as vg_dynadag
    import visgraph.renderers.svgrend as vg_svgrend

    g = vg_graphcore.HierarchicalGraph()

    g.addNode('A', rootnode=True)
    g.addNode('B')
    g.addNode('C')
    g.addNode('D')

    g.addNode('E')
    g.addNode('F')
    g.addNode('G')

    g.addEdge('A','B')
    g.addEdge('A','C')

    g.addEdge('B','D')
    g.addEdge('B','E')

    g.addEdge('C','F')
    g.addEdge('C','G')

    layout = vg_dynadag.DynadagLayout(g)
    rend = vg_svgrend.SvgGraphRenderer(g, 'test.svg')

    layout.renderGraph(rend)
