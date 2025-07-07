# assume this cube is 3x3x3
# also assuming using speffz notation
# im doing red as the front face tho
import math
class Cube:
    def __init__(self, scramble:str =''):
        # colours of the edges
        self.edge = {
            'a' : 'white',
            'b' : 'white',
            'c' : 'white',
            'd' : 'white',
            'e' : 'green',
            'f' : 'green',
            'g' : 'green',
            'h' : 'green',
            'i' : 'red',
            'j' : 'red',
            'k' : 'red',
            'l' : 'red',
            'm' : 'blue',
            'n' : 'blue',
            'o' : 'blue',
            'p' : 'blue',
            'q' : 'orange',
            'r' : 'orange',
            's' : 'orange',
            't' : 'orange',
            'u' : 'yellow',
            'v' : 'yellow',
            'w' : 'yellow',
            'x' : 'yellow'}
        # colours of the corners
        self.corner = {
            'a' : 'white',
            'b' : 'white',
            'c' : 'white',
            'd' : 'white',
            'e' : 'green',
            'f' : 'green',
            'g' : 'green',
            'h' : 'green',
            'i' : 'red',
            'j' : 'red',
            'k' : 'red',
            'l' : 'red',
            'm' : 'blue',
            'n' : 'blue',
            'o' : 'blue',
            'p' : 'blue',
            'q' : 'orange',
            'r' : 'orange',
            's' : 'orange',
            't' : 'orange',
            'u' : 'yellow',
            'v' : 'yellow',
            'w' : 'yellow',
            'x' : 'yellow',
        }   
        # corresponding edges of other edges
        self.cor_edge = {
            'a' : 'q',
            'b' : 'm',
            'c' : 'i',
            'd' : 'e',
            'e' : 'd',
            'f' : 'l',
            'g' : 'x',
            'h' : 'r',
            'i' : 'c',
            'j' : 'p',
            'k' : 'u',
            'l' : 'f',
            'm' : 'b',
            'n' : 't',
            'o' : 'v',
            'p' : 'j',
            'q' : 'a',
            'r' : 'h',
            's' : 'w',
            't' : 'n',
            'u' : 'k',
            'v' : 'o',
            'w' : 's',
            'x' : 'g',
        }
        self.cor_corner = {
            'a' : ['e','r'],
            'b' : ['n','q'],
            'c' : ['j','m'],
            'd' : ['f','i'],
            'e' : ['a','r'],
            'f' : ['d','i'],
            'g' : ['l','u'],
            'h' : ['s','x'],
            'i' : ['d','f'],
            'j' : ['c','m'],
            'k' : ['p','v'],
            'l' : ['g','u'],
            'm' : ['c','j'],
            'n' : ['b','q'],
            'o' : ['t','w'],
            'p' : ['k','v'],
            'q' : ['b','n'],
            'r' : ['a','e'],
            's' : ['h','x'],
            't' : ['o','w'],
            'u' : ['g','l'],
            'v' : ['k','p'],
            'w' : ['o','t'],
            'x' : ['h','s'],
        }

    def scramble(self, scramble:str):
        scramble_map = {
            "F" : self.f_turn,
            "F'" : self.fp_turn,
            "R" : self.r_turn,
            "R'" : self.rp_turn,
            "L" : self.l_turn,
            "L'" : self.lp_turn,
            "U" : self.u_turn,
            "U'" : self.up_turn,
            "D" : self.d_turn,
            "D'" : self.dp_turn,
            "B" : self.b_turn,
            "B'" : self.bp_turn,
            "U2" : lambda: (self.u_turn(), self.u_turn()),
            "D2" : lambda: (self.d_turn(), self.d_turn()),
            "L2" : lambda: (self.l_turn(), self.l_turn()),
            "R2" : lambda: (self.r_turn(), self.r_turn()),
            "F2" : lambda: (self.f_turn(), self.f_turn()),
            "B2" : lambda: (self.b_turn(), self.b_turn()),
        }

        for move in scramble.split():
            move = move.upper()
            if move in scramble_map:
                scramble_map[move]()


    # rotating the edges the other way
    # the edges are inputted in clockwise order
    # te edges are the edges on the turning face. also inputted clockwise
    def rotate_edge(self, e1, e2, e3, e4, te1, te2, te3, te4):
        self.edge[e1], self.edge[e2], self.edge[e3], self.edge[e4] = self.edge[e4], self.edge[e1], self.edge[e2], self.edge[e3]
        self.edge[te1], self.edge[te2], self.edge[te3], self.edge[te4] = self.edge[te4], self.edge[te1], self.edge[te2], self.edge[te3]

    # rotating the edges but in reverse
    # the edges are inputted in clockwise order
    def rotate_prime_edge(self, e1, e2, e3, e4, te1, te2, te3, te4):
        self.edge[e1], self.edge[e2], self.edge[e3], self.edge[e4] = self.edge[e2], self.edge[e3], self.edge[e4], self.edge[e1]
        self.edge[te1], self.edge[te2], self.edge[te3], self.edge[te4] = self.edge[te2], self.edge[te3], self.edge[te4], self.edge[te1]

    # rotating the corners in clockwise rotation
    # the corners are inputted in clockwise order
    def rotate_corner(self, c1, c2, c3, c4, c5, c6, c7, c8, tc1, tc2, tc3, tc4):
        self.corner[c1], self.corner[c2], self.corner[c3], self.corner[c4], self.corner[c5], self.corner[c6], self.corner[c7], self.corner[c8] = self.corner[c7], self.corner[c8], self.corner[c1], self.corner[c2], self.corner[c3], self.corner[c4], self.corner[c5], self.corner[c6]
        self.corner[tc1], self.corner[tc2], self.corner[tc3], self.corner[tc4] = self.corner[tc4], self.corner[tc1], self.corner[tc2], self.corner[tc3]

    # rotating the corners in counter clockwise rotation    
    def rotate_prime_corner(self, c1, c2, c3, c4, c5, c6, c7, c8, tc1, tc2, tc3, tc4):
        self.corner[c1], self.corner[c2], self.corner[c3], self.corner[c4], self.corner[c5], self.corner[c6], self.corner[c7], self.corner[c8] = self.corner[c3], self.corner[c4], self.corner[c5], self.corner[c6], self.corner[c7], self.corner[c8], self.corner[c1], self.corner[c2]
        self.corner[tc1], self.corner[tc2], self.corner[tc3], self.corner[tc4] = self.corner[tc2], self.corner[tc3], self.corner[tc4], self.corner[tc1]

    # this assumes the front face is red
    # regular turn not prime
    def f_turn(self):
        self.rotate_edge('c', 'p', 'u', 'f', self.cor_edge['c'], self.cor_edge['p'], self.cor_edge['u'], self.cor_edge['f'])
        self.rotate_corner('d', 'c', 'm', 'p', 'v', 'u', 'g', 'f', 'i', 'j', 'k', 'l')

    # f prime turn
    def fp_turn(self):
        self.rotate_prime_edge('c', 'p', 'u', 'f', self.cor_edge['c'], self.cor_edge['p'], self.cor_edge['u'], self.cor_edge['f'])
        self.rotate_prime_corner('d', 'c', 'm', 'p', 'v', 'u', 'g', 'f', 'i', 'j', 'k', 'l')
    
    # right turn
    def r_turn(self):
        self.rotate_edge('j', 'b', 't', 'v', self.cor_edge['j'], self.cor_edge['b'], self.cor_edge['t'], self.cor_edge['v'])
        self.rotate_corner('c', 'b', 'q', 't', 'w', 'v', 'k', 'j','m', 'n', 'o', 'p')

    
    # right prime turn
    def rp_turn(self):
        self.rotate_prime_edge('j', 'b', 't', 'v', self.cor_edge['j'], self.cor_edge['b'], self.cor_edge['t'], self.cor_edge['v'])
        self.rotate_prime_corner('c', 'b', 'q', 't', 'w', 'v', 'k', 'j','m', 'n', 'o', 'p')

    # left turn 
    def l_turn(self):
        self.rotate_edge('d', 'l', 'x', 'r', self.cor_edge['d'], self.cor_edge['l'], self.cor_edge['x'], self.cor_edge['r'])
        self.rotate_corner('a', 'd', 'i', 'l', 'u', 'x', 's', 'r', 'e', 'f', 'g', 'h')     
    
    # left prime turn
    def lp_turn(self):
        self.rotate_prime_edge('d', 'l', 'x', 'r', self.cor_edge['d'], self.cor_edge['l'], self.cor_edge['x'], self.cor_edge['r'])
        self.rotate_prime_corner('a', 'd', 'i', 'l', 'u', 'x', 's', 'r', 'e', 'f', 'g', 'h')  

    # u turn
    def u_turn(self):
        self.rotate_edge('i', 'e', 'q', 'm', self.cor_edge['i'], self.cor_edge['e'], self.cor_edge['q'], self.cor_edge['m'])
        self.rotate_corner('j', 'i', 'f', 'e', 'r', 'q', 'n', 'm', 'a', 'b', 'c', 'd')
    # u prime turn
    def up_turn(self):
        self.rotate_prime_edge('i', 'e', 'q', 'm', self.cor_edge['i'], self.cor_edge['e'], self.cor_edge['q'], self.cor_edge['m'])
        self.rotate_prime_corner('j', 'i', 'f', 'e', 'r', 'q', 'n', 'm','a', 'b', 'c', 'd')
    
    # down turn
    def d_turn(self):  
        self.rotate_edge('k', 'o', 's', 'g', self.cor_edge['k'], self.cor_edge['o'], self.cor_edge['s'], self.cor_edge['g'])
        self.rotate_corner('l', 'k', 'p', 'o', 't', 's', 'h', 'g', 'u', 'v', 'w', 'x')
    
    # down prime turn 
    def dp_turn(self):
        self.rotate_prime_edge('k', 'o', 's', 'g', self.cor_edge['k'], self.cor_edge['o'], self.cor_edge['s'], self.cor_edge['g'])
        self.rotate_prime_corner('l', 'k', 'p', 'o', 't', 's', 'h', 'g', 'u', 'v', 'w', 'x')

    # back turn 
    def b_turn(self):
        self.rotate_edge('a', 'h', 'w', 'n', self.cor_edge['a'], self.cor_edge['h'], self.cor_edge['w'], self.cor_edge['n'])
        self.rotate_corner('b', 'a', 'e', 'h', 'x', 'w', 'o', 'n','q', 'r', 's', 't')


    # back prime turn
    def bp_turn(self):
        self.rotate_prime_edge('a', 'h', 'w', 'n', self.cor_edge['a'], self.cor_edge['h'], self.cor_edge['w'], self.cor_edge['n'])
        self.rotate_prime_corner('b', 'a', 'e', 'h', 'x', 'w', 'o', 'n','q', 'r', 's', 't')

    def edge_swap_alg(self, new_edge):
        self.edge['b'], self.edge['m'], self.edge[new_edge], self.edge[self.cor_edge[new_edge]] = self.edge[new_edge], self.edge[self.cor_edge[new_edge]], self.edge['b'], self.edge['m']
        # self.corner['b'], self.corner['n'], self.corner['q'], self.corner['c'], self.corner['j'], self.corner['m'] = self.corner['c'], self.corner['j'], self.corner['m'], self.corner['b'], self.corner['n'], self.corner['q']

    # check solved edges
    def check_solved_edges(self):
        solved = []
        unsolved = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x']
        # brute force check for edges 
        # checking first layer edges (white edges in this case)
        if self.edge['a'] == 'white' and self.edge[self.cor_edge['a']] == 'orange':
            solved.append('a')
            solved.append(self.cor_edge['a'])
        if self.edge['b'] == 'white' and self.edge[self.cor_edge['b']] == 'blue':
            solved.append('b')
            solved.append(self.cor_edge['b'])
        if self.edge['c'] == 'white' and self.edge[self.cor_edge['c']] == 'red':
            solved.append('c')
            solved.append(self.cor_edge['c'])
        if self.edge['d'] == 'white' and self.edge[self.cor_edge['d']] == 'green':
            solved.append('d')
            solved.append(self.cor_edge['d'])

        # checking second layer edges (headlights in this case)
        if self.edge['l'] == 'red' and self.edge[self.cor_edge['l']] == 'green':
            solved.append('l')
            solved.append(self.cor_edge['l'])
        if self.edge['j'] == 'red' and self.edge[self.cor_edge['j']] == 'blue':
            solved.append('j')
            solved.append(self.cor_edge['j'])
        if self.edge['t'] == 'orange' and self.edge[self.cor_edge['t']] == 'blue':
            solved.append('t')
            solved.append(self.cor_edge['t'])
        if self.edge['r'] == 'orange' and self.edge[self.cor_edge['r']] == 'green':
            solved.append('r')
            solved.append(self.cor_edge['r'])

        # checking third layer edges (yellow edges in this case)
        if self.edge['u'] == 'yellow' and self.edge[self.cor_edge['u']] == 'red':
            solved.append('u')
            solved.append(self.cor_edge['u'])
        if self.edge['v'] == 'yellow' and self.edge[self.cor_edge['v']] == 'blue':
            solved.append('v')
            solved.append(self.cor_edge['v'])
        if self.edge['w'] == 'yellow' and self.edge[self.cor_edge['w']] == 'orange':
            solved.append('w')
            solved.append(self.cor_edge['w'])
        if self.edge['x'] == 'yellow' and self.edge[self.cor_edge['x']] == 'green':
            solved.append('x')
            solved.append(self.cor_edge['x'])

        for i in solved:
            unsolved.remove(i)
        return solved, unsolved

    def solve_edges_new():
        solved , unsolved = self.check_solved_edges()
        sequence = ''

        # these 2 variables are used to denote which is the face of the edge is our main face
        # they also change every time we solve an edge
        buffer = 'b'
        cor_buffer = 'm'

        # input the buffer into the corresponding dict to find which edge to swap with
        # use dict based on corresponding buffer edge
        yellow_cor_buffer = {
            'green' : 'g', # this means if the buffer is green, then swap with g
            'red' : 'k',
            'blue' : 'o',
            'orange' : 's',
        }

        red_cor_buffer = {
            'green' : 'f',
            'yellow' : 'u',
            'blue' : 'p',
            'white' : 'c',
        }

        green_cor_buffer = {
            'red' : 'l',
            'yellow' : 'x',
            'orange' : 'r',
            'white' : 'd',
        }

        orange_cor_buffer = {
            'blue' : 'n',
            'yellow' : 'w',
            'green' : 'h',
            'white' : 'a',
        }

        white_cor_buffer = {
            'red' : 'i',
            'green' : 'e',
            'blue' : 'm',
            'orange' : 'q',
        }

        blue_cor_buffer = {
            'red' : 'j',
            'yellow' : 'v',
            'orange' : 't',
            'white' : 'b',
        }
w       colour_cor_dicts = {
            'yellow': yellow_cor_buffer,
            'green' : green_cor_buffer,
            'red'   : red_cor_buffer,
            'orange': orange_cor_buffer,
            "white" : white_cor_buffer,
            "blue"  : blue_cor_buffer
        }   
        while len(solved) != 24:
            new_edge = colour_cor_dicts[cor_buffer][buffer]
            cor_new_edge = self.cor_edge[new_edge]

            self.edge_swap_alg(new_edge)

            sequence += new_edge
            solved.append(new_edge)
            solved.append(cor_new_edge)

    # this is the old version for the solve_edges function
    # getting output for solved edges string
    def solve_edges(self):
        solved , unsolved = self.check_solved_edges()
        sequence = ''

        # these 2 variables are used to denote which is the face of the edge is our main face
        # they also change every time we solve an edge
        buffer = 'b'
        cor_buffer = 'm'

        # input the buffer into the corresponding dict to find which edge to swap with
        # use dict based on corresponding buffer edge
        yellow_cor_buffer = {
            'green' : 'g', # this means if the buffer is green, and the cor_buffer is yellow, then swap with g 
            'red' : 'k',
            'blue' : 'o',
            'orange' : 's',
        }

        red_cor_buffer = {
            'green' : 'f',
            'yellow' : 'u',
            'blue' : 'p',
            'white' : 'c',
        }

        green_cor_buffer = {
            'red' : 'l',
            'yellow' : 'x',
            'orange' : 'r',
            'white' : 'd',
        }

        orange_cor_buffer = {
            'blue' : 'n',
            'yellow' : 'w',
            'green' : 'h',
            'white' : 'a',
        }

        white_cor_buffer = {
            'red' : 'i',
            'green' : 'e',
            'blue' : 'm',
            'orange' : 'q',
        }

        blue_cor_buffer = {
            'red' : 'j',
            'yellow' : 'v',
            'orange' : 't',
            'white' : 'b',
        }


        # solving alg here
        for i in unsolved:
            # first checking if our buffer is solved
            # if (buffer in solved) and ((self.edge['b'] == 'white' and self.edge[self.cor_edge['b']] == 'blue') or (self.edge['b'] == 'blue' and self.edge[self.cor_edge['b']] == 'white')):
            # if (self.edge['b'] == 'white' and self.edge[self.cor_edge['b']] == 'blue') or (self.edge['b'] == 'blue' and self.edge[self.cor_edge['b']] == 'white'):
            if (self.edge[buffer] == 'white' and self.edge[cor_buffer] == 'blue') or (self.edge[buffer] == 'blue' and self.edge[cor_buffer] == 'white'):

                # checking easy replacements for the buffer
                if 'd' not in solved:
                    sequence += 'd'
                elif 'l' not in solved:
                    sequence += 'l'
                elif 'r' not in solved:
                    sequence += 'r'
                elif 'x' not in solved:
                    sequence += 'x'
                else:
                    sequence += i
                buffer = sequence[-1]
                solved.append(buffer)
                cor_buffer = self.cor_edge[buffer]
                continue

            else: # since the buffer is not solved, we can check where the buffer sticker is supposed to be
                if self.edge[cor_buffer] == 'yellow':
                    sequence += yellow_cor_buffer[self.edge[buffer]]
                elif self.edge[cor_buffer] == 'red':
                    sequence += red_cor_buffer[self.edge[buffer]]
                elif self.edge[cor_buffer] == 'green':
                    sequence += green_cor_buffer[self.edge[buffer]]
                elif self.edge[cor_buffer] == 'orange':
                    sequence += orange_cor_buffer[self.edge[buffer]]
                elif self.edge[cor_buffer] == 'white':
                    sequence += white_cor_buffer[self.edge[buffer]]
                elif self.edge[cor_buffer] == 'blue':   
                    sequence += blue_cor_buffer[self.edge[buffer]]
                buffer = sequence[-1]
                solved.append(buffer)
                cor_buffer = self.cor_edge[buffer]


        if len(solved) == 24:            
            # formatting the sequence
            half = math.ceil(len(sequence) / 2)
            # this makes sure that the outputted sequence doesn't cut off the last move
            if half % 2 == 1:
                half += 1
            sequence = sequence[:half]
            formatted = ' '.join(sequence[i:i+2] for i in range(0, len(sequence), 2))
            return formatted

# sd vc al jn hk gf
            

# cube = Cube()
# cube.scramble("L F' D F L' F'")
# print(f"Sequence: {cube.solve_edges()}")
# solved, unsolved = cube.check_solved_edges()
# print(f"Solved: {solved}")
# print(f"Unsolved: {unsolved}")
# print(f"Total unsolved edges: {len(unsolved)/2}")

# print("CUBE EDGES\n-----------")
# for i in cube.edge.keys():
#     print(f"{i}: {cube.edge[i]}")
# # print(list(cube.edge.keys()))

# print("\nCUBE CORNERS\n-----------")
# for i in cube.corner.keys():
#     print(f"{i}: {cube.corner[i]}")

# Old Scrambles
# scramble = "L F' D F L' F'"
# scramble = "F L' F L U2 B L' D R2 F2 B2 U2 L2 B2 U F2 R' D2 B'"


scramble = "B' U2 L' F' D' R2 F2 B2 U2 L2 B2 U F2 R' D2 B'"
cube1 = Cube()
cube1.scramble(scramble=scramble)
print(f"Sequence: {cube1.solve_edges()}")
print(f"Unsolved: {cube1.check_solved_edges()[1]}")

#hello this is a test

# cube = Cube()
# cube.edge_swap_alg('d')
# print(cube.edge)