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
        for symbol in input_string:
            if (self.current_state, symbol, self.stack[-1]) in self.transition:
                next_state, pop_symbol, push_symbols = self.transition[(self.current_state, symbol, self.stack[-1])]

                # Pindah ke state berikutnya
                self.current_state = next_state

                # Pop simbol dari stack
                if pop_symbol != 'ε':
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
                # if (self.current_state != 'q1'): #coba coba 
                print(f"Error: No transition for ({self.current_state}, {symbol}, {self.stack[-1]}).")
                return False


        popped = self.stack.pop()
        if(popped != initial_stack_symbol):
            return False
        print(self.stack)
        return self.is_accepted()

# Contoh penggunaan
states = {'q0', 'q1', 'q2','end','endhead'} #q0 start alias html #q1 kondisi dalam html
input_alphabet = {'<','h','t','m','l','>','/'}
stack_alphabet = {'Z', '1'}
transition = {
    ('q0', '<', 'Z'): ('q0', 'ε', '<'),
    ('q0', 'h', '<'): ('q0', 'ε', 'h'),
    ('q0', 't', 'h'): ('q0', 'ε', 't'),
    ('q0', 'm', 't'): ('q0', 'ε', 'm'),
    ('q0', 'l', 'm'): ('q0', 'ε', 'l'),
    ('q0', '>', 'l'): ('q1', 'ε', '>'),


    ('q1', '<', '>'): ('cek', '>', '>'), # gk berubah


    #html to /html q1 -> end
    ('cek','/','>') : ('end','>','ε'),
    ('end','h','l') : ('end','l','ε'),
    ('end','t','m') : ('end','m','ε'),
    ('end','m','t') : ('end','t','ε'),
    ('end','l','h') : ('end','h','ε'),
    ('end','>','<') : ('end','<','ε'),


    #html to head q1 -> q2
    ('cek','h','>') : ('q2','ε','<h'),
    ('q2','e','h') : ('q2','ε','e'),
    ('q2','a','e') : ('q2','ε','a'),
    ('q2','d','a') : ('q2','ε','d'),
    ('q2','>','d') : ('q2','ε','>'),
  



    #head q2 to end head -> balik ke q1(didalam html)
    ('q2','<','>') : ('q2','>','>'),
    ('q2','/','>') : ('endhead','>','ε'),
    ('endhead','h','d') : ('endhead','d','ε'),
    ('endhead','e','a') : ('endhead','a','ε'),
    ('endhead','a','e') : ('endhead','e','ε'),
    ('endhead','d','h') : ('endhead','h','ε'),
    ('endhead','>','<') : ('q1','<','ε'),
    
    
    

    



    ('q1', '', 'Z'): ('q2', 'ε', 'ε'),  # Penambahan transisi untuk membaca epsilon saat stack kosong
}
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
result_string = "".join(splittedcontent)

print(result_string)

result = pda.process_input(result_string)

if result:
    print(f"Input '{result_string}' is accepted.")
else:
    print(f"Input '{result_string}' is not accepted.")
