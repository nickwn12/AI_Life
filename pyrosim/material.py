from pyrosim.commonFunctions import Save_Whitespace


class MATERIAL:

    def __init__(self, colorName="Cyan", rgb=[1, 1, 1]):

        self.depth = 3

        self.string1 = '<material name="' + colorName + '">'

        self.string2 = '    <color rgba="0 ' + \
            str(rgb[0]) + ' '+str(rgb[1]) + ' ' + str(rgb[2]) + '"/>'

        self.string3 = '</material>'

    def Save(self, f):

        Save_Whitespace(self.depth, f)

        f.write(self.string1 + '\n')

        Save_Whitespace(self.depth, f)

        f.write(self.string2 + '\n')

        Save_Whitespace(self.depth, f)

        f.write(self.string3 + '\n')
