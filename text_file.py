var1 = open('test_file.txt', 'r', encoding='utf-8')
var1.close()
var2 = open('test_file1.txt', 'w', encoding='utf-8')
var2.write('Hello, Stepik!')
var2.close()
var3 = open('test_file2.txt', 'a', encoding='utf-8')
var3.write('privet!')
var3.close()

