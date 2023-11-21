import os
class PDA:
    def __init__(self, states, input_alphabet, stack_alphabet, transition, start_state, initial_stack_symbol):
        self.states = states
        self.input_alphabet = input_alphabet
        self.stack_alphabet = stack_alphabet
        self.transition = transition
        self.start_state = start_state
        self.current_state = start_state
        self.initial_stack_symbol = initial_stack_symbol
        self.stack = [initial_stack_symbol]

    def is_accepted(self):
        return not self.stack
    def process_input(self, input_string):


        #MULAI LOOPING
        for symbol in input_string:
            if ((self.current_state, symbol, self.stack[-1]) in self.transition and self.current_state in self.states):
                next_state, pop_symbol, push_symbols = self.transition[(self.current_state, symbol, self.stack[-1])]

                # Pindah ke state berikutnya
                self.current_state = next_state

                # Pop simbol dari stack

                if len(pop_symbol) >= 1 and pop_symbol != 'ε':
                    for symb in pop_symbol:
                        popped = self.stack.pop()
                        if popped != pop_symbol:
                            print(f"Error: Expected '{pop_symbol}' on top of stack, but got '{popped}'.")
                            return False
                # Push simbol-simbol ke stack
                if push_symbols != 'ε':
                    self.stack.extend(push_symbols)



                # Print stack setiap kali berubah
                print(f"Current State: {self.current_state}")
                print(self.stack)
            else:
                if (self.current_state != 'qpetikbody' and self.current_state != 'qpetikhead'and self.current_state != 'qpetikhtml'
                    and self.current_state != 'qpetiktitle' and self.current_state != 'qpetiklinkhead' and self.current_state != 'qkutiplinkhead'):   #Handler ignorance
                    print(f"Error: No transition for ({self.current_state}, {symbol}, {self.stack[-1]}).")
                    return False
                


        #TERAKHIR BANGET
        popped = self.stack.pop()
        if(popped != initial_stack_symbol):
            return False
        print(self.stack)
        return self.is_accepted()

# Contoh penggunaan
states = {'q0','qcek','qhead','endhtml','qatrhtml','qclasshtml','qpetikhtml','qidhtml','qstylehtml'
          ,'qatrbody','qclassbody','qpetikbody','qstylebody','qidbody','qbody','endbody',
          'qatrhead','qclasshead','qpetikhead','qidhead','qstylehead,','qcekhead','endhead',
          'qtitle','qatrtitle','endtitle','qclasstitle','qstyletitle','qidtitle','qpetiktitle'
          ,'qlinkhead','qatrlinkhead','qkutiplinkhead','qclasslinkhead','qstylelinkhead','qidlinkhead','qhreflinkhead','qpetiklinkhead'} 
input_alphabet = {'<','h','t','m','l','>','/'}
stack_alphabet = {'Z', '1'}
transition = {
            
           
            #==============================HTML==============================
            ('q0', '<', 'Z'): ('q0', 'ε', '<'),
            ('q0', 'h', '<'): ('q0', 'ε', 'h'),
            ('q0', 't', 'h'): ('q0', 'ε', 't'),
            ('q0', 'm', 't'): ('q0', 'ε', 'm'),
            ('q0', 'l', 'm'): ('q0', 'ε', 'l'),
            ('q0','>','l') : ('qcek' ,'ε','X>'),
            ('q0',' ','l'): ('qatrhtml','ε','X'),
            ('qatrhtml',' ','X') : ('qatrhtml' , 'ε','ε'),
            ('qatrhtml','>','X'): ('qcek','ε','>'),


            ('endbody', '<', '>'): ('endhtml', '>', 'ε'),
            ('endhtml', '/', 'X'): ('endhtml', 'X', 'ε'),
            ('endhtml', 'h', 'l'): ('endhtml', 'l', 'ε'),
            ('endhtml', 't', 'm'): ('endhtml', 'm', 'ε'),
            ('endhtml', 'm', 't'): ('endhtml', 't', 'ε'),
            ('endhtml', 'l', 'h'): ('endhtml', 'h', 'ε'),
            ('endhtml', '>', '<'): ('qhtml', '<', 'ε'),
            ('qhtml', 'Z', 'ε'): ('qhtml', 'ε', 'ε'),

            #Q Attribute HTML
            ('qatrhtml','c','X') : ('qclasshtml','ε', 'c'),
            ('qclasshtml','l','c') : ('qclasshtml','ε','l'),
            ('qclasshtml','a','l') : ('qclasshtml','ε','a'),
            ('qclasshtml','s','a') : ('qclasshtml','a','ε'),
            ('qclasshtml','s','l') : ('qclasshtml','l','ε'),
            ('qclasshtml','=','c') : ('qclasshtml','c','ε'),
            ('qclasshtml','"','X') : ('qpetikhtml','ε','"'),
            ('qpetikhtml','"','"') : ('qatrhtml' , '"','ε'),

            ('qatrhtml','s','X') : ('qstylehtml','ε', 's'),
            ('qstylehtml','t','s') : ('qstylehtml','ε','t'),
            ('qstylehtml','y','t') : ('qstylehtml','ε','y'),
            ('qstylehtml','l','y') : ('qstylehtml','y','ε'),
            ('qstylehtml','e','t') : ('qstylehtml','t','ε'),
            ('qstylehtml','=','s') : ('qstylehtml','s','ε'),
            ('qstylehtml','"','X') : ('qpetikhtml','ε','"'),
            ('qpetikhtml','"','"') : ('qatrhtml' , '"','ε'),

            ('qatrhtml','i','X') : ('qidhtml','ε', 'i'),
            ('qidhtml','d','i') : ('qidhtml','i','ε'),
            ('qidhtml','=','X') : ('qidhtml','ε','ε'),
            ('qidhtml','"','X') : ('qpetikhtml','ε','"'),
            ('qpetikhtml','"','"') : ('qatrhtml' , '"','ε'),


            #==============================BODY==============================
            ('qcek',' ','>'):('qcek','ε','ε'),
            ('qcek', '<', '>'): ('qcek', 'ε', '<'),
            ('qcek', 'b', '<'): ('qbody', 'ε', 'b'),
            ('qbody', 'o', 'b'): ('qbody', 'ε', 'o'),
            ('qbody', 'd', 'o'): ('qbody', 'ε', 'd'),
            ('qbody', 'y', 'd'): ('qbody', 'ε', 'y'),
            ('qbody', '>', 'y'): ('qbody', 'ε', 'X>'),
            ('qbody',' ','y'): ('qatrbody','ε','X'),
            ('qatrbody',' ','X') : ('qatrbody', 'ε' , 'ε'), #handler spasi di atribute
            ('qatrbody', '>', 'X'): ('qbody', 'ε', '>'),

            ('qbody',' ','>') : ('qbody','ε','ε'),
            ('qbody', '<', '>'): ('qbody', '>', 'ε'),
            ('qbody', '/', 'X'): ('endbody', 'X', 'ε'),
            ('endbody', 'b', 'y'): ('endbody', 'y', 'ε'),
            ('endbody', 'o', 'd'): ('endbody', 'd', 'ε'),
            ('endbody', 'd', 'o'): ('endbody', 'o', 'ε'),
            ('endbody', 'y', 'b'): ('endbody', 'b', 'ε'),
            ('endbody', '>', '<'): ('endbody', '<', 'ε'),
            ('endbody', ' ', '>'): ('endbody', 'ε', 'ε'),

            #Q Attribute Body
            ('qatrbody','c','X') : ('qclassbody','ε', 'c'),
            ('qclassbody','l','c') : ('qclassbody','ε','l'),
            ('qclassbody','a','l') : ('qclassbody','ε','a'),
            ('qclassbody','s','a') : ('qclassbody','a','ε'),
            ('qclassbody','s','l') : ('qclassbody','l','ε'),
            ('qclassbody','=','c') : ('qclassbody','c','ε'),
            ('qclassbody','"','X') : ('qpetikbody','ε','"'),
            ('qpetikbody','"','"') : ('qatrbody' , '"','ε'),

            ('qatrbody','s','X') : ('qstylebody','ε', 's'),
            ('qstylebody','t','s') : ('qstylebody','ε','t'),
            ('qstylebody','y','t') : ('qstylebody','ε','y'),
            ('qstylebody','l','y') : ('qstylebody','y','ε'),
            ('qstylebody','e','t') : ('qstylebody','t','ε'),
            ('qstylebody','=','s') : ('qstylebody','s','ε'),
            ('qstylebody','"','X') : ('qpetikbody','ε','"'),
            ('qpetikbody','"','"') : ('qatrbody' , '"','ε'),

            ('qatrbody','i','X') : ('qidbody','ε', 'i'),
            ('qidbody','d','i') : ('qidbody','i','ε'),
            ('qidbody','=','X') : ('qidbody','ε','ε'),
            ('qidbody','"','X') : ('qpetikbody','ε','"'),
            ('qpetikbody','"','"') : ('qatrbody' , '"','ε'),


            #==============================HEAD============================
            ('qcek', '<', '>'): ('qcek', 'ε', '<'),
            ('qcek', 'h', '<'): ('qhead', 'ε', 'h'),
            ('qhead', 'e', 'h'): ('qhead', 'ε', 'e'),
            ('qhead', 'a', 'e'): ('qhead', 'ε', 'a'),
            ('qhead', 'd', 'a'): ('qhead', 'ε', 'd'),
            ('qhead', '>', 'd'): ('qcekhead', 'ε', 'X>'),
            ('qhead', ' ','d') : ('qatrhead' ,'ε','X'),
            ('qatrhead',' ','X') : ('qatrhead', 'ε' , 'ε'),
            ('qatrhead', '>', 'X'): ('qcekhead', 'ε', '>'),


            ('qcekhead', '/', '>'): ('endhead', '>', 'ε'),
            ('endhead', 'h', 'X'): ('endhead', 'X', 'ε'),
            ('endhead', 'e', 'd'): ('endhead', 'd', 'ε'),
            ('endhead', 'a', 'a'): ('endhead', 'a', 'ε'),
            ('endhead', 'd', 'e'): ('endhead', 'e', 'ε'),
            ('endhead', '>', 'h'): ('qcek', 'h', 'ε'),
            ('qcek', ' ', '<'): ('qcek', '<', 'ε'),
            

             #Q Attribute Head
            ('qatrhead','c','X') : ('qclasshead','ε', 'c'),
            ('qclasshead','l','c') : ('qclasshead','ε','l'),
            ('qclasshead','a','l') : ('qclasshead','ε','a'),
            ('qclasshead','s','a') : ('qclasshead','a','ε'),
            ('qclasshead','s','l') : ('qclasshead','l','ε'),
            ('qclasshead','=','c') : ('qclasshead','c','ε'),
            ('qclasshead','"','X') : ('qpetikhead','ε','"'),
            ('qpetikhead','"','"') : ('qatrhead' , '"','ε'),

            ('qatrhead','s','X') : ('qstylehead','ε', 's'),
            ('qstylehead','t','s') : ('qstylehead','ε','t'),
            ('qstylehead','y','t') : ('qstylehead','ε','y'),
            ('qstylehead','l','y') : ('qstylehead','y','ε'),
            ('qstylehead','e','t') : ('qstylehead','t','ε'),
            ('qstylehead','=','s') : ('qstylehead','s','ε'),
            ('qstylehead','"','X') : ('qpetikhead','ε','"'),
            ('qpetikhead','"','"') : ('qatrhead' , '"','ε'),

            ('qatrhead','i','X') : ('qidhead','ε', 'i'),
            ('qidhead','d','i') : ('qidhead','i','ε'),
            ('qidhead','=','X') : ('qidhead','ε','ε'),
            ('qidhead','"','X') : ('qpetikhead','ε','"'),
            ('qpetikhead','"','"') : ('qatrhead' , '"','ε'),

            #==============================TITLE============================ (HEAD)
            ('qcekhead',' ','>') : ('qcekhead','ε','ε'), #handle spasi antar tag
            ('qcekhead', '<', '>'): ('qcekhead', 'ε', 'ε'),
            ('qcekhead', 't', '>'): ('qtitle', 'ε', '<t'),
            ('qtitle', 'i', 't'): ('qtitle', 'ε', 'i'),
            ('qtitle', 't', 'i'): ('qtitle', 'ε', 't'),
            ('qtitle', 'l', 't'): ('qtitle', 'ε', 'l'),
            ('qtitle', 'e', 'l'): ('qtitle', 'ε', 'e'),
            ('qtitle', ' ', 'e'): ('qatrtitle', 'ε', 'X'),
            ('qtitle', '>', 'e'): ('qtitle', 'ε', 'X>'),
            ('qatrtitle','>','X') : ('qtitle','ε','>'),
            ('qatrtitle',' ','X') : ('qatrtitle','ε', 'ε'), #Handler apabila ada spasi di atribute

            ('qtitle',' ','>') : ('qtitle','ε','ε'),
            ('qtitle','<','>') : ('endtitle','>','ε'),
            ('endtitle','/','X') : ('endtitle','X','ε'),
            ('endtitle','t','e') : ('endtitle','e','ε'),
            ('endtitle','i','l') : ('endtitle','l','ε'),
            ('endtitle','t','t') : ('endtitle','t','ε'),
            ('endtitle','l','i') : ('endtitle','i','ε'),
            ('endtitle','e','t') : ('endtitle','t','ε'),
            ('endtitle','>','<') : ('qcekhead','<','ε'),
            ('endtitle', ' ', '>'): ('endtitle', 'ε', 'ε'),

             #Q Attribute Title
            ('qatrtitle','c','X') : ('qclasstitle','ε', 'c'),
            ('qclasstitle','l','c') : ('qclasstitle','ε','l'),
            ('qclasstitle','a','l') : ('qclasstitle','ε','a'),
            ('qclasstitle','s','a') : ('qclasstitle','a','ε'),
            ('qclasstitle','s','l') : ('qclasstitle','l','ε'),
            ('qclasstitle','=','c') : ('qclasstitle','c','ε'),
            ('qclasstitle','"','X') : ('qpetiktitle','ε','"'),
            ('qpetiktitle','"','"') : ('qatrtitle' , '"','ε'),

            ('qatrtitle','s','X') : ('qstyletitle','ε', 's'),
            ('qstyletitle','t','s') : ('qstyletitle','ε','t'),
            ('qstyletitle','y','t') : ('qstyletitle','ε','y'),
            ('qstyletitle','l','y') : ('qstyletitle','y','ε'),
            ('qstyletitle','e','t') : ('qstyletitle','t','ε'),
            ('qstyletitle','=','s') : ('qstyletitle','s','ε'),
            ('qstyletitle','"','X') : ('qpetiktitle','ε','"'),
            ('qpetiktitle','"','"') : ('qatrtitle' , '"','ε'),

            
            ('qatrtitle','i','X') : ('qidtitle','ε', 'i'),
            ('qidtitle','d','i') : ('qidtitle','i','ε'),
            ('qidtitle','=','X') : ('qidtitle','ε','ε'),
            ('qidtitle','"','X') : ('qpetiktitle','ε','"'),
            ('qpetiktitle','"','"') : ('qatrtitle' , '"','ε'),


            #==============================LINK============================ (HEAD,BODY)
            ('qcekhead',' ','>') : ('qcekhead','ε','ε'), #handle spasi antar tag
            ('qcekhead', '<', '>'): ('qcekhead', 'ε', 'ε'),
            ('qcekhead', 'l', '>'): ('qlinkhead', 'ε', '<l'),
            ('qlinkhead', 'i', 'l'): ('qlinkhead', 'ε', 'i'),
            ('qlinkhead', 'n', 'i'): ('qlinkhead', 'ε', 'n'),
            ('qlinkhead', 'k', 'n'): ('qlinkhead', 'ε', 'k'),
            ('qlinkhead',' ', 'k'): ('qatrlinkhead','ε' ,'ε'),
            ('qatrlinkhead','r', 'k'): ('qlinkhead','k' ,'ε'),
            ('qlinkhead','e', 'n'): ('qlinkhead','n' ,'ε'),
            ('qlinkhead','l', 'i'): ('qlinkhead','i' ,'ε'),
            ('qlinkhead','=', 'l'): ('qlinkhead','l' ,'ε'),
            ('qlinkhead','"', '<'): ('qkutiplinkhead','ε' ,'"'),
            ('qkutiplinkhead','"', '"'): ('qlinkhead','"' ,'ε'),
            ('qlinkhead',' ','<') : ('qatrlinkhead','ε','ε'),
            ('qlinkhead','>','<') : ('qcekhead','<','ε'),
            ('qatrlinkhead','>','<') : ('qcekhead','<','ε'),
            ('qatrlinkhead',' ','<') : ('qatrlinkhead','ε', 'ε'), #Handler apabila ada spasi di atribute

            #Q Attribute Link
            ('qatrlinkhead','h','<') : ('qhreflinkhead','ε', 'h'),
            ('qhreflinkhead','r','h') : ('qhreflinkhead','ε','r'),
            ('qhreflinkhead','e','r') : ('qhreflinkhead','r','ε'),
            ('qhreflinkhead','f','h') : ('qhreflinkhead','h','ε'),
            ('qhreflinkhead','=','<') : ('qhreflinkhead','ε','ε'),
            ('qhreflinkhead','"','<') : ('qpetiklinkhead','ε','"'),
            ('qpetiklinkhead','"','"') : ('qatrlinkhead' , '"','ε'),
           
            

            
            ('qatrlinkhead','c','<') : ('qclasslinkhead','ε', 'c'),
            ('qclasslinkhead','l','c') : ('qclasslinkhead','ε','l'),
            ('qclasslinkhead','a','l') : ('qclasslinkhead','ε','a'),
            ('qclasslinkhead','s','a') : ('qclasslinkhead','a','ε'),
            ('qclasslinkhead','s','l') : ('qclasslinkhead','l','ε'),
            ('qclasslinkhead','=','c') : ('qclasslinkhead','c','ε'),
            ('qclasslinkhead','"','<') : ('qpetiklinkhead','ε','"'),
            ('qpetiklinkhead','"','"') : ('qatrlinkhead' , '"','ε'),

            ('qatrlinkhead','s','<') : ('qstylelinkhead','ε', 's'),
            ('qstylelinkhead','t','s') : ('qstylelinkhead','ε','t'),
            ('qstylelinkhead','y','t') : ('qstylelinkhead','ε','y'),
            ('qstylelinkhead','l','y') : ('qstylelinkhead','y','ε'),
            ('qstylelinkhead','e','t') : ('qstylelinkhead','t','ε'),
            ('qstylelinkhead','=','s') : ('qstylelinkhead','s','ε'),
            ('qstylelinkhead','"','<') : ('qpetiklinkhead','ε','"'),
            ('qpetiklinkhead','"','"') : ('qatrlinkhead' , '"','ε'),

            
            ('qatrlinkhead','i','<') : ('qidlinkhead','ε', 'i'),
            ('qidlinkhead','d','i') : ('qidlinkhead','i','ε'),
            ('qidlinkhead','=','<') : ('qidlinkhead','ε','ε'),
            ('qidlinkhead','"','<') : ('qpetiklinkhead','ε','"'),
            ('qpetiklinkhead','"','"') : ('qatrlinkhead' , '"','ε'),
           


            
            
           
         
}


    # ('q1', '<', '>'): ('cek', '>', '>'), # gk berubah


    # #html to /html q1 -> end
    # ('cek','/','>') : ('end','>','ε'),
    # ('end','h','l') : ('end','l','ε'),
    # ('end','t','m') : ('end','m','ε'),
    # ('end','m','t') : ('end','t','ε'),
    # ('end','l','h') : ('end','h','ε'),
    # ('end','>','<') : ('end','<','ε'),


    # #html to head q1 -> q2
    # ('cek','h','>') : ('q2','ε','<h'),
    # ('q2','e','h') : ('q2','ε','e'),
    # ('q2','a','e') : ('q2','ε','a'),
    # ('q2','d','a') : ('q2','ε','d'),
    # ('q2','>','d') : ('q2','ε','>'),
  

    # #head q2 to end head -> balik ke q1(didalam html)
    # ('q2','<','>') : ('q2','>','>'),
    # ('q2','/','>') : ('endhead','>','ε'),
    # ('endhead','h','d') : ('endhead','d','ε'),
    # ('endhead','e','a') : ('endhead','a','ε'),
    # ('endhead','a','e') : ('endhead','e','ε'),
    # ('endhead','d','h') : ('endhead','h','ε'),
    # ('endhead','>','<') : ('q1','<','ε'),

    # #head to body
    # ('cek','h','>') : ('q2','ε','<h'),
    # ('q2','e','h') : ('q2','ε','e'),
    # ('q2','a','e') : ('q2','ε','a'),
    # ('q2','d','a') : ('q2','ε','d'),
    # ('q2','>','d') : ('q2','ε','>'),
  

    # #body to endbody
    # ('q2','<','>') : ('q2','>','>'),
    # ('q2','/','>') : ('endhead','>','ε'),
    # ('endhead','h','d') : ('endhead','d','ε'),
    # ('endhead','e','a') : ('endhead','a','ε'),
    # ('endhead','a','e') : ('endhead','e','ε'),
    # ('endhead','d','h') : ('endhead','h','ε'),
    # ('endhead','>','<') : ('q1','<','ε'),
    
    
    # ('q1', '', 'Z'): ('q2', 'ε', 'ε'),  # Penambahan transisi untuk membaca epsilon saat stack kosong
start_state = 'q0'
initial_stack_symbol = 'Z'

pda = PDA(states, input_alphabet, stack_alphabet, transition, start_state, initial_stack_symbol)

# Mendapatkan path dari direktori saat ini
current_directory = os.getcwd()
# Path dari direktori parent untuk file atau direktori tertentu
file_path = os.path.join(current_directory,'src', 'example.html')

with open(file_path, 'r') as file:
    # Membaca seluruh konten file
    html_content = file.read()

# Sekarang, variabel html_content berisi seluruh string dari file HTML
splittedcontent = html_content.split()
result_string = " ".join(splittedcontent)

print(result_string)

result = pda.process_input(result_string)

if result:
    print(f"Input '{result_string}' is accepted.")
else:
    print(f"Input '{result_string}' is not accepted.")
