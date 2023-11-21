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
                if (self.current_state != 'qpetikbody' and self.current_state != 'qpetikhead'and self.current_state != 'qpetikhtml' ):   #Handler ignorance
                    print(f"Error: No transition for ({self.current_state}, {symbol}, {self.stack[-1]}).")
                    return False
                


        #TERAKHIR BANGET
        popped = self.stack.pop()
        if(popped != initial_stack_symbol):
            return False
        print(self.stack)
        return self.is_accepted()

# Contoh penggunaan
states = {'q0','endhead','qcek','qhead','qbody','endbody','endhtml'
          ,'qatrbody','qclassbody','qpetikbody','qstylebody','qidbody',
          'qatrhead','qclasshead','qpetikhead','qidhead','qstylehead'} 
input_alphabet = {'<','h','t','m','l','>','/'}
stack_alphabet = {'Z', '1'}
transition = {
            
           
            #==============================HTML==============================
            ('q0', '<', 'Z'): ('q0', 'ε', '<'),
            ('q0', 'h', '<'): ('q0', 'ε', 'h'),
            ('q0', 't', 'h'): ('q0', 'ε', 't'),
            ('q0', 'm', 't'): ('q0', 'ε', 'm'),
            ('q0', 'l', 'm'): ('q0', 'ε', 'lX'),
            ('q0',' ','l'): ('q0','ε','ε'),
            ('q0', '>', 'X'): ('qcek', 'ε', '>'),

    
            ('endbody', '<', '>'): ('endhtml', '>', 'ε'),
            ('endhtml', '/', 'X'): ('endhtml', 'X', 'ε'),
            ('endhtml', 'h', 'l'): ('endhtml', 'l', 'ε'),
            ('endhtml', 't', 'm'): ('endhtml', 'm', 'ε'),
            ('endhtml', 'm', 't'): ('endhtml', 't', 'ε'),
            ('endhtml', 'l', 'h'): ('endhtml', 'h', 'ε'),
            ('endhtml', '>', '<'): ('qhtml', '<', 'ε'),
            ('qhtml', 'Z', 'ε'): ('qhtml', 'ε', 'ε'),


            #==============================BODY==============================
            ('qcek',' ','>'):('qcek','ε','ε'),
            ('qcek', '<', '>'): ('qcek', 'ε', '<'),
            ('qcek', 'b', '<'): ('qbody', 'ε', 'b'),
            ('qbody', 'o', 'b'): ('qbody', 'ε', 'o'),
            ('qbody', 'd', 'o'): ('qbody', 'ε', 'd'),
            ('qbody', 'y', 'd'): ('qbody', 'ε', 'y'),
            ('qbody', '>', 'y'): ('qbody', 'ε', 'X>'),
            ('qbody',' ','y'): ('qatrbody','ε','X'),
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


            #==============================HEAD==============================
            ('qcek', '<', '>'): ('qcek', 'ε', '<'),
            ('qcek', 'h', '<'): ('qhead', 'ε', 'h'),
            ('qhead', 'e', 'h'): ('qhead', 'ε', 'e'),
            ('qhead', 'a', 'e'): ('qhead', 'ε', 'a'),
            ('qhead', 'd', 'a'): ('qhead', 'ε', 'd'),
            ('qhead', '>', 'd'): ('qhead', 'ε', 'X>'),
            ('qhead', ' ','d') : ('qatrhead' ,'ε','X'),
            ('qatrhead',' ','X') : ('qatrhead', 'ε' , 'ε'),
            ('qatrhead', '>', 'X'): ('qhead', 'ε', '>'),

            ('qhead',' ','>') : ('qhead','ε','ε'),
            ('qhead', '<', '>'): ('endhead', '>', 'ε'),
            ('endhead', '/', 'X'): ('endhead', 'X', 'ε'),
            ('endhead', 'h', 'd'): ('endhead', 'd', 'ε'),
            ('endhead', 'e', 'a'): ('endhead', 'a', 'ε'),
            ('endhead', 'a', 'e'): ('endhead', 'e', 'ε'),
            ('endhead', 'd', 'h'): ('endhead', 'h', 'ε'),
            ('endhead', '>', '<'): ('qcek', '<', 'ε'),

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
