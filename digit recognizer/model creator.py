import random
from datetime import datetime

pool = []

class Neuron:
    def __init__(self, data, children=[], parents=[], weight=randfloat(0,1)):
        self.data = data
        self.id = time.time_ns()
        self.children = children
        self.parents = parents
        self.weight = weight
    def get(self):
        return self.value

def create_neuron(data):
    new = Neuron(data)
    pool.append(new)
    return new.id

def link_neuron(child,parent):
    child.parents.append(parent.id)
    parent.children.append(child.id)

def delink_neuron(child,parent):
    if parent.id in child.parents and child.id in parent.children:
        parent.children.remove(child.id)
        child.parents.remove(parent.id)
    else:
        print ("neurons not linked")

def create_weights_pool():
    return {pool:[],inputs:[],outputs:[]}