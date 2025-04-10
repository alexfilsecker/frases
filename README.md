# Motivational Frases API

I was bored so I created this very very simple API that returns a random motivational frase.

## Deployment

This project has `Docker` configured so to run it just do

```bash
docker compose up -d
```

This will mount the `frases` container in your computer. To retrieve a frase do:

```bash
curl localhost:8005
```

This will show a motivational frase.

## Customization

You can customize the frases by changing the [`frases.txt`](./frases.txt) file.

## Alias

To enhance your experience you can add the following line to your `.zshrc` file:

```.zshrc
alias hola='curl localhost:8005'
```

Where hola could be any alias you would like!
