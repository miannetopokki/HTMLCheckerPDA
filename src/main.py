import os
import sys
import ast

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
            transition_key = (self.current_state, symbol, self.stack[-1])
            transition_tuple = self.transition.get(transition_key)

            
            if transition_tuple is not None:
                next_state, pop_symbol, push_symbols = transition_tuple

           
            if ((self.current_state, symbol, self.stack[-1]) in self.transition and self.current_state in self.states):
                next_state, pop_symbol, push_symbols = self.transition[(self.current_state, symbol, self.stack[-1])]

                
                # Pindah ke state berikutnya
                self.current_state = next_state

                # Pop simbol dari stack

                if len(pop_symbol) >= 1 and pop_symbol != 'ε':
                    for symb in pop_symbol:
                        popped = self.stack.pop()
                        if popped != pop_symbol:
                            return False
                # Push simbol-simbol ke stack
                if push_symbols != 'ε':
                    self.stack.extend(push_symbols)
                print(self.stack)
        

            elif (self.current_state != 'qcommentIN' and self.current_state != 'qpetikbody' and self.current_state != 'qpetikhead'and self.current_state != 'qpetikhtml'
                    and self.current_state != 'qpetiktitle' and self.current_state != 'qpetiklinkhead' and self.current_state != 'qkutiplinkhead'
                    and self.current_state != 'qdiv' and self.current_state != 'qpetikhr' and self.current_state != 'qpetika'
                    and self.current_state != "qpetikdiv" and self.current_state != "qtitle"  and self.current_state != "qhIN" 
                    and self.current_state != "qcekscript"and self.current_state != "qpetikp"  and self.current_state != "qpIN"
                    and self.current_state != "qstrongIN"
                    and self.current_state != "qabbrIN"
                    and self.current_state != "qsmallIN"
                    and self.current_state != "qbIN"
                    and self.current_state != "qemIN"
                    and self.current_state != "qcekform"
                    and self.current_state != "qpetikbutton"
                    and self.current_state != "qpetikform"
                    and self.current_state != "qpetiktable"
                    and self.current_state != "qpetikh"
                    and self.current_state != "qpetiktd"
                    and self.current_state != "qpetikth"
                    and self.current_state != "qpetiktr"
                    and self.current_state != "qth"
                    and self.current_state != "qtd"
                    and self.current_state != "qtr"
                    and self.current_state != "qpetikinput"
                    and self.current_state != "qpetikimg"
                    and self.current_state != "qpetiksrcimg"
                    and self.current_state != "qpetikhr"
                    and self.current_state != "qpetika"
                    and self.current_state != "qbutton"
                    and self.current_state != "qformIN"
                    and self.current_state != "qa"):   #Handler ignorance
                        print(f"Error: No transition for ({self.current_state}, {symbol}, {self.stack[-1]}).")
                        return False
                

        #TERAKHIR BANGET
       
        popped = self.stack.pop()
        if(popped != initial_stack_symbol):
            return False
        return self.is_accepted()


# Dapatkan argumen dari baris perintah
if len(sys.argv) != 3:
    print("Usage: python main.py <pda_file> <input_file>")
    sys.exit(1)

pda_file = sys.argv[1]
input_file = sys.argv[2]


# Periksa apakah kedua file eksis sebelum melanjutkan
if not os.path.exists(pda_file):
    print(f"Error: File '{pda_file}' not found.")
    sys.exit(1)

if not os.path.exists(input_file):
    print(f"Error: File '{input_file}' not found.")
    sys.exit(1)

# Baca isi dari file pda_file dan input_file
with open(pda_file, 'r') as file:
    pda_content = file.read()

exec(pda_content)

pda = PDA(states, input_alphabet, stack_alphabet, transition, start_state, initial_stack_symbol)


with open(input_file, 'r') as file:
    # Membaca seluruh konten file
    html_content = file.read()

result_string = ""
inside_tag = False

for char in html_content:
    if char == '<':
        inside_tag = True
        result_string += ' ' + char
    elif char == '>':
        inside_tag = False
        result_string += char + ' '
    else:
        result_string += char
# Sekarang, variabel html_content berisi seluruh string dari file HTML

result_string = " ".join(result_string.split())

result = pda.process_input(result_string)

if result:
    print(f"Accepted.")
else:
    print(f"Rejected.")
