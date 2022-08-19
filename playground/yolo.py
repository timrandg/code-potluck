#!/usr/bin/env python
import click

@click.command()
@click.option('--count', default=2, help='Number of greetings.')
@click.option('--reverse', '-r', is_flag=True, help='Reverse the message.')
@click.option('--novowel', '-nv', is_flag=True, help='Reverse the message.')
def yolo(count, reverse, novowel):
    message = 'yolo'
    if novowel:
        message_x = ''
        for letter in message:
            if letter not in 'aeiou':
                message_x += letter
        message = message_x
    if reverse:
        message = message[::-1]
    for _ in range(count):
       click.echo(message)

if __name__ == '__main__':
    yolo()

