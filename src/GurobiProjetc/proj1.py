#!/usr/bin/env python3.7

# Copyright 2021, Gurobi Optimization, LLC

# This example formulates and solves the following simple MIP model:
#  maximize
#        x +   y + 2 z
#  subject to
#        x + 2 y + 3 z <= 4
#        x +   y       >= 1
#        x, y, z binary

import gurobipy as gp
from gurobipy import GRB

from flask import Flask
from flask_restplus import Api, Resource

from src.server.instance import server

app, api = server.app, server.api


results_db = [{'vars':[]}]


















@api.route("/gurobi")
class GurobiExemple1(Resource):
    """description of class"""
    def _GurobiExe(self,):
        # Gurobi exemple solver
        try:

            # Create a new model
            m = gp.Model("mip1")

            # Create variables
            x = m.addVar(vtype=GRB.BINARY, name="x")
            y = m.addVar(vtype=GRB.BINARY, name="y")
            z = m.addVar(vtype=GRB.BINARY, name="z")

            # Set objective
            m.setObjective(x + y + 2 * z, GRB.MAXIMIZE)

            # Add constraint: x + 2 y + 3 z <= 4
            m.addConstr(x + 2 * y + 3 * z <= 4, "c0")

            # Add constraint: x + y >= 1
            m.addConstr(x + y >= 1, "c1")

            # Optimize model
            m.optimize()

            for v in m.getVars():
                #print('%s %g' % (v.varName, v.x))
                results_db[0]['vars'].append({str(v.varName): v.x})

            #print('Obj: %g' % m.objVal)
            results_db[0]['Obj'] = m.objVal

        except gp.GurobiError as e:
            #print('Error code ' + str(e.errno) + ': ' + str(e))
            results_db[0]['erro'] = 'Error code ' + str(e.errno) + ': ' + str(e)

        except AttributeError:
            #print('Encountered an attribute error')
            results_db[0]['erro'] = 'Encountered an attribute error'
        return results_db


    

    def get(self, ):
        
        return self._GurobiExe()#results_db
    def post(self, ):
        response = api.payload
        
        #results_db.append(response)
        results_db = self._GurobiExe()
        #results_db.append(response)
        return results_db, 200
