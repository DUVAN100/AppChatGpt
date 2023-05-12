import openai 
import typer  
from rich import print  
from rich.table import Table

def main():
    openai.api_key = "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"
    print("💬 [bold green]ChatGPT API en Python[/bold green]")
    table = Table("Comando", "Descripción")
    table.add_row("exit", "Salir de la aplicación")
    table.add_row("new", "Crear una nueva conversación")
    print(table)
    context = {"role": "system",
               "content": "Eres un asistente muy útil."}
    messages = [context]
    
    while True:
        content = __prompt()
        if content == "new":
            print("🆕 New coveration created ")
            messages = [context]
            content = __prompt()

        messages.append({"role": "user", "content": content})
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo",  messages=messages)
        response_content = response.choices[0].message.content
        messages.append({"role": "assistant", "content": response_content})
        print(f"[bold green]> [/bold green] [green]{response_content}[/green]")

def __prompt() -> str:
    prompt = typer.prompt("\n¿Ask me ? ")
    if prompt == "exit":
        exit = typer.confirm("✋ ¿Are your sure?")
        if exit:
            print("👋 ¡Bye!")
            raise typer.Abort()
        return __prompt()
    return prompt

if __name__ == "__main__":
    typer.run(main)