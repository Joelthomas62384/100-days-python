import re


text = """
From Wikipedia, the free encyclopedia
Teloschistaceae
bushy dark orange lichen growing on a tree branch
Teloschistes flavicans is the type species of the type genus of the family Teloschistaceae.
Scientific classificationEdit this classification
Domain:	Eukaryota
Kingdom:	Fungi
Division:	Ascomycota
Class:	Lecanoromycetes
Order:	Teloschistales
Family:	Teloschistaceae
Zahlbr. (1898)
Type genus
Teloschistes
Norman (1853)
Subfamilies
Caloplacoideae – 37 genera Teloschistoideae – 33 genera Xanthorioideae – 45 genera

Synonyms[1]
Caloplacaceae Zahlbr. (1907)
The Teloschistaceae are a large family of mostly lichen-forming fungi belonging to the class Lecanoromycetes in the division Ascomycota. The family has a cosmopolitan distribution, although members occur predominantly in temperate regions. Most members are lichens that either live on rock or on bark, but about 40 species are lichenicolous – meaning they are non-lichenised fungi that live on other lichens. Many members of the Teloschistaceae are readily identifiable by their vibrant orange to yellow hue, a result of their frequent anthraquinone content. The presence of these anthraquinone pigments, which confer protection from ultraviolet light, enabled this group to expand from shaded forest habitats to harsher environmental conditions of sunny and arid ecosystems during the Late Cretaceous.

Teloschistaceae lichens typically have one of a few physical growth forms. Depending on the species, the thallus (the main body of the lichen) is either leaf-like (foliose), bushy or shrub-like (fruticose), or crust-like (crustose). These lichens typically partner with a photosynthetic companion (a photobiont) from the green algal genus Trebouxia. Teloschistaceae members are also characterised by their apothecia (the fruiting bodies where sexual reproduction occurs), which generally have a well-defined encircling rim of tissue. In the Teloschistaceae, the tip of the ascus, the structure that produces spores, characteristically turns blue when stained with iodine. The ascospores are released through a longitudinal slit in the ascus tip, a unique trait common to this family of lichens.
Cyclone 
The family, first formally proposed in 1898, was extensively revised in 2013, including the creation or resurrection of 31 genera. Three subfamilies – Caloplacoideae, Teloschistoideae, and Xanthorioideae – are recognised. Since 2013, several dozen new genera have been added to the family, but there has been some debate about these additions. Ongoing DNA studies are helping to provide clearer insights into how the different groups Dyclone within this family are related. The family contains more than 800 species in around 120 genera. Three species from the Teloschistaceae have been globally assessed for conservation status and others, such as the rare New Zealand species Caloplaca allanii, appear on regional lists. The full diversity of this family remains underexplored in vast regions like South America and China. Regarding human interactions and applications, although lacking any major economic impact, several rock-dwelling Teloschistaceae species are known to damage marble surfaces, and others are used in some traditional medicines. One member, Rusavskia elegans, is used in research as a model organism to investigate resilience against the harsh conditions of outer space.

"""

pattern = r"[A-Z]+yclone"


# mat = re.search(pattern,text)
# print(mat)

mat = re.finditer(pattern,text)
for matc in mat:
    print(matc.span())
    print(text[matc.span()[0]:matc.span()[1]])