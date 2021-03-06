""" Tests for the command class. """

from .fixtures import *

from metapipe.parser import Parser
from metapipe.models import *


def test_eval_1():
    parser = Parser(overall)

    cmds = parser.consume()
    print(cmds[0].parts)
    cmds[0].eval()[0].eval().should.equal('/usr/bin/python somescript.py -i somefile.1 somefile.2 somefile.3 -o metapipe.1.1.output -fgh somefile.txt')
    
    
def test_eval_2():
    parser = Parser(overall)
    cmds = parser.consume()

    cmds[0].eval()[1].eval().should.equal('/usr/bin/python somescript.py -i somefile.4 somefile.5 somefile.6 -o metapipe.1.2.output -fgh somefile.txt')
    
    
def test_eval_3():
    parser = Parser(overall)
    cmds = parser.consume()
    old_commands = []
    for cmd in cmds[0:1]:
        old_commands.extend(cmd.eval())

    cmd = cmds[1].eval()[0]
    cmd.update_dependent_files(old_commands)
    cmd.eval().should.equal('/usr/bin/bash somescript.sh -i metapipe.1.1.output -o metapipe.2.1.output -fgh somefile.txt')


def test_eval_4():
    parser = Parser(overall)
    cmds = parser.consume()
    old_commands = []
    for cmd in cmds[0:1]:
        old_commands.extend(cmd.eval())

    cmd = cmds[1].eval()[1]
    cmd.update_dependent_files(old_commands)
    print([i.filename for i in cmd.input_parts])
    cmd.eval().should.equal('/usr/bin/bash somescript.sh -i metapipe.1.2.output -o metapipe.2.2.output -fgh somefile.txt')
   
    
def test_eval_5():
    parser = Parser(overall)
    cmds = parser.consume()
    old_commands = []
    for cmd in cmds[0:2]:
        old_commands.extend(cmd.eval())

    cmd = cmds[2].eval()[0]
    cmd.update_dependent_files(old_commands)
    cmd.eval().should.equal('/usr/bin/ruby somescript.rb -i metapipe.2.1.output >> somefile')


def test_eval_6():
    parser = Parser(overall)
    cmds = parser.consume()
    old_commands = []
    for cmd in cmds[0:2]:
        old_commands.extend(cmd.eval())

    cmd = cmds[2].eval()[1]
    cmd.update_dependent_files(old_commands)
    print([i.filename for i in cmd.input_parts])
    cmd.eval().should.equal('/usr/bin/ruby somescript.rb -i metapipe.2.2.output >> somefile')
    

def test_eval_7():
    parser = Parser(overall)
    cmds = parser.consume()
    old_commands = []
    for cmd in cmds[0:2]:
        old_commands.extend(cmd.eval())

    cmd = cmds[2].eval()[2]
    cmd.update_dependent_files(old_commands)
    cmd.eval().should.equal('/usr/bin/ruby somescript.rb -i metapipe.1.1.output metapipe.1.2.output >> somefile')


def test_eval_8():
    parser = Parser(overall)
    cmds = parser.consume()
    old_commands = []
    for cmd in cmds[0:3]:
        old_commands.extend(cmd.eval())

    cmd = cmds[3].eval()[0]
    cmd.update_dependent_files(old_commands)
    print([i.filename for i in cmd.input_parts])
    cmd.eval().should.equal('cut -f *.counts > something.file')


def test_eval_9():
    parser = Parser(overall)
    cmds = parser.consume()
    old_commands = []
    for cmd in cmds[0:4]:
        old_commands.extend(cmd.eval())

    cmd = cmds[4].eval()[0]
    cmd.update_dependent_files(old_commands)
    print([i.filename for i in cmd.input_parts])
    cmd.eval().should.equal('paste *.counts > some.file # some.file')
    

def test_eval_10():
    parser = Parser(overall)
    cmds = parser.consume()
    old_commands = []
    for cmd in cmds[0:5]:
        old_commands.extend(cmd.eval())

    cmd = cmds[5].eval()[0]
    cmd.update_dependent_files(old_commands)
    print([i.filename for i in cmd.input_parts])
    cmd.eval().should.equal('./somescript somefile.1 somefile.2 somefile.3 somefile.4')
    

def test_eval_11():
    parser = Parser(overall)
    cmds = parser.consume()
    old_commands = []
    for cmd in cmds[0:5]:
        old_commands.extend(cmd.eval())

    cmd = cmds[5].eval()[1]
    cmd.update_dependent_files(old_commands)
    print([i.filename for i in cmd.input_parts])
    cmd.eval().should.equal('./somescript somefile.1.counts somefile.2.counts somefile.3.counts somefile.4.counts')
    

def test_eval_12():
    parser = Parser(overall)
    cmds = parser.consume()
    old_commands = []
    for cmd in cmds[0:6]:
        old_commands.extend(cmd.eval())

    cmd = cmds[6].eval()[0]
    cmd.update_dependent_files(old_commands)
    print([i.filename for i in cmd.input_parts])
    cmd.eval().should.equal('/usr/bin/ruby somescript.rb -i somefile.4.counts')
    

def test_eval_13():
    parser = Parser(overall)
    cmds = parser.consume()
    old_commands = []
    for cmd in cmds[0:6]:
        old_commands.extend(cmd.eval())

    cmd = cmds[6].eval()[1]
    cmd.update_dependent_files(old_commands)
    print([i.filename for i in cmd.input_parts])
    cmd.eval().should.equal('/usr/bin/ruby somescript.rb -i somefile.3.counts')
    
    
def test_eval_14():
    parser = Parser(overall)
    cmds = parser.consume()
    old_commands = []
    for cmd in cmds[0:6]:
        old_commands.extend(cmd.eval())

    cmd = cmds[6].eval()[2]
    cmd.update_dependent_files(old_commands)
    print([i.filename for i in cmd.input_parts])
    cmd.eval().should.equal('/usr/bin/ruby somescript.rb -i somefile.2.counts')
   
   
def test_eval_14():
    parser = Parser(overall)
    cmds = parser.consume()
    old_commands = []
    for cmd in cmds[0:6]:
        old_commands.extend(cmd.eval())

    cmd = cmds[6].eval()[3]
    cmd.update_dependent_files(old_commands)
    print([i.filename for i in cmd.input_parts])
    cmd.eval().should.equal('/usr/bin/ruby somescript.rb -i somefile.1.counts')
    
  
def test_eval_15():
    parser = Parser(overall)
    cmds = parser.consume()
    old_commands = []
    for cmd in cmds[0:7]:
        old_commands.extend(cmd.eval())

    cmd = cmds[7].eval()[0]
    cmd.update_dependent_files(old_commands)
    print([i.eval() for i in cmd.output_parts])
    cmd.eval().should.equal('/usr/bin/python somescript.py -i somefile.1.counts somefile.2.counts somefile.3.counts somefile.4.counts # *.bam')
    

def test_eval_16():
    parser = Parser(overall)
    cmds = parser.consume()
    old_commands = []
    for cmd in cmds[0:8]:
        old_commands.extend(cmd.eval())

    cmd = cmds[8].eval()[0]
    cmd.update_dependent_files(old_commands)
    print([i.eval() for i in cmd.input_parts])
    cmd.eval().should.equal('cat somefile.1.bam somefile.2.bam somefile.bam')


def test_eval_16_deps():
    parser = Parser(overall)
    cmds = parser.consume()
    old_commands = []
    for cmd in cmds[0:8]:
        old_commands.extend(cmd.eval())

    cmd = cmds[8].eval()[0]
    cmd.update_dependent_files(old_commands)
    #print([i.eval() for i in cmd.input_parts])
    cmd.dependencies.should.have.length_of(1)
