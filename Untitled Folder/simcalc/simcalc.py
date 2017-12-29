#! /bin/python
import click

@click.command()
@click.option('--add', nargs=2, type=float)
@click.option('--sub', nargs=2, type=float)
@click.option('--mul', nargs=2, type=float)
@click.option('--div', nargs=2, type=float)
def simcalc(add,sub,mul,div):
	if add and not sub and not mul and not div: # if --add
		print (add[0]+add[1]) 
	elif sub and not add and not mul and not div:# if --sub
		print (sub[0]-sub[1])
	elif mul and not add and not sub and not div:# if --mul
		print (mul[0]*mul[1])
	elif div and not add and not sub and not mul:# if --div
		print (div[0]/div[1])

if __name__ == '__main__':
    simcalc()

