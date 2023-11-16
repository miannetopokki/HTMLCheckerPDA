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
                print(f"Current State: {self.current_state}, Current Stack: {''.join(self.stack)}")
                print(self.stack)
            else:
                print(f"Error: No transition for ({self.current_state}, {symbol}, {self.stack[-1]}).")
                return False
        popped = self.stack.pop()
        if(popped != initial_stack_symbol):
            return False

        return self.is_accepted()

# Contoh penggunaan
states = {'q0', 'q1', 'q2'}
input_alphabet = {'a', 'b'}
stack_alphabet = {'Z', '1'}
transition = {
    ('q0', 'a', 'Z'): ('q0', 'ε', '1'),
    ('q0', 'a', '1'): ('q0', 'ε', '1'),
    ('q0', 'b', '1'): ('q1', '1', 'ε'),
    ('q1', 'b', '1'): ('q1', '1', 'ε'),
    ('q1', '', 'Z'): ('q2', 'ε', 'ε'),  # Penambahan transisi untuk membaca epsilon saat stack kosong
}
start_state = 'q0'
initial_stack_symbol = 'Z'

pda = PDA(states, input_alphabet, stack_alphabet, transition, start_state, initial_stack_symbol)

input_string = 'aabb'
result = pda.process_input(input_string)

if result:
    print(f"Input '{input_string}' is accepted.")
else:
    print(f"Input '{input_string}' is not accepted.")
