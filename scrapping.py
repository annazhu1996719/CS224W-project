import xmltodict
import csv

def parseXML(index): 
	xmlfile = str(index) + ".gexf"
	try:
		with open(xmlfile) as fd:
		    doc = xmltodict.parse(fd.read())
	except FileNotFoundError:
		return
	nodes = doc["gexf"]["graph"]["nodes"]["node"]
	edges = doc["gexf"]["graph"]["edges"]["edge"]
	n = len(nodes)
	with open("nodes/"+ str(index) + "_nodes.txt", mode='w') as csv_file:
		node_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		for i in range(n):
			node = nodes[i]
			if i == 0:
				node_writer.writerow(['id', 'label', 'eccentricity', 'closnesscentrality', 'betweenesscentrality', 'degree', 'componentnumber', 'modularity_class'])
			node_writer.writerow([node['@id'], node['@label'], node['attvalues']['attvalue'][1]['@value'], node['attvalues']['attvalue'][2]['@value'], node['attvalues']['attvalue'][3]['@value'], node['attvalues']['attvalue'][4]['@value'], node['attvalues']['attvalue'][5]['@value'], node['attvalues']['attvalue'][6]['@value']])
	n = len(edges)
	with open("edges/"+ str(index) + "_edges.txt", mode='w') as csv_file:
		edge_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		if type(edges) != type([]):
			if i == 0:
				edge_writer.writerow(['source', 'target', 'weight'])
			edge_writer.writerow([edges["@source"], edges["@target"], edges['attvalues']['attvalue'][0]['@value']])
			return
		for i in range(n):
			edge = edges[i]
			if i == 0:
				edge_writer.writerow(['source', 'target', 'weight'])
			edge_writer.writerow([edge["@source"], edge["@target"], edge['attvalues']['attvalue'][0]['@value']])


for k in range(1,915):
	print(k)
	parseXML(k)