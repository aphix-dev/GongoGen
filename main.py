import templateParser

## Will rewrite a go template into a go file using the 
def RewriteGoFile(fileName, fileType):
    pass


##################### MAIN ########################
file = open("V:/.Code/GongoGen/templates/test.go", "w")
print("*** GongoGen ***")
baseDir = input("Project Directory (structure like C:/...): ")
modelFolder = input("Model/Schema Folder Name: ")
modelName = input("Model Name (lowercase): ")
file = open(f"{baseDir}/{modelFolder}/{modelName}.go", 'w')

file.write(f"package {modelFolder}\n\n")
file.write(f"type {modelName.capitalize()} struct " + '{\n')

## model struct generation code
fields = {}
print()
while True:
    field = input("Field (click <enter> if none): ")
    if field == "": break
    t = input("Field Type: ")
    fields[field] = t
for v in fields:
    varType = fields[v]
    vc = v.capitalize()
    file.write(f'\t{vc} {varType} `bson:"{vc}" json:"{vc}"`\n')
file.write('}\n')


"""
with open('./templates/get.go') as file:
    print(file.readline())
"""