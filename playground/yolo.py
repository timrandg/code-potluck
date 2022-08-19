#!/usr/bin/env python
import click

@click.command()
@click.option('--count', default=2, help='Number of greetings.')
@click.option('--reverse', '-r', is_flag=True, help='Reverse the message.')
def yolo(count, reverse):
    message = 'yolo'
    if reverse:
        message = message[::-1]
    for _ in range(count):
       click.echo(message)

if __name__ == '__main__':
    yolo()

