# -*- coding: utf-8 -*-
from __future__ import with_statement # Siempre debe ir primero
from pyke import knowledge_engine, krb_traceback, goal
import sys

engine = knowledge_engine.engine(__file__)
engine.activate('fc_bateria')

# Compilar
fc_goal = goal.compile('bateria.tipo_bateria($nombre, $peso, $precio, $material, $mensaje)')

def fc_test():
    print("[TIPO] Forward Chaining")
    print("[INFO] Iniciando...")
    with fc_goal.prove(engine) as gen:
        i = 0
        for vars, plan in gen:
            i += 1
            print("[" + str(i) + "]", vars['mensaje'], ": ", vars['nombre'], ' | ', vars['peso'], ' | ', vars['precio'], ' | ', vars['material'])
    print("[INFO] Terminado !!!\n")

def bc_test():
    print("[TIPO] Backward Chaining")
    print("[INFO] Iniciando...")
    with engine.prove_goal(
        'bateria.tipo_bateria($nombre, $peso, $precio, $material, $mensaje)'
    ) as gen:
        i = 0
        for vars, plan in gen:
            i += 1
            print("[" + str(i) + "]", vars['mensaje'], ": ", vars['nombre'], ' | ', vars['peso'], ' | ', vars['precio'], ' | ', vars['material'])
    print("[INFO] Terminado !!!\n\n")

def fc_questions_test():
    engine.reset()
    print("[INFO] Haciendo preguntas...")
    engine.activate('fc_bateria_questions')
    with engine.prove_goal(
        'bateria.tipo_bateria($nombre, $peso, $precio, $material, $mensaje)'
    ) as gen:
        i = 0
        for vars, plan in gen:
            i += 1
            print("[" + str(i) + "]", vars['mensaje'], ": ", vars['nombre'], ' | ', vars['peso'], ' | ', vars['precio'], ' | ', vars['material'])
        if i <= 0:
            print("[INFO] No pude reconocer el tipo de bateria")
    print("\n[INFO] Terminado !!!\n")

if __name__ == "__main__":
    fc_test()
    bc_test()
    fc_questions_test()