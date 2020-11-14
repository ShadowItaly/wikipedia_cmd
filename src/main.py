import wikipedia
from rich.console import Console
from rich.table import Table
from rich.progress import Progress
from rich.panel import Panel


def process(query,console):
    """Processes a given query and fetches the results from wikipedia.

    Keyword arguments:
    query -- The query 
    imag -- the imaginary part (default 0.0)
    """
    with Progress() as progress:
        # Querying the search to wikipedia and showing a progress bar for it
        task = progress.add_task("Querying wikipedia for \""+query+"\"",total=1)
        ls = wikipedia.search(query)
        progress.advance(task)

    
    # Displaying a table which shows the 10 results we got from wikipedia
    table = Table(show_header=True,header_style='bold magenta')

    # Show the source of the results
    table.add_column("Source wikipedia")
    for x in range(len(ls)):
        table.add_row("[bold yellow]"+str(x)+"[/bold yellow] "+ls[x])

    # Show the table
    console.print(table)
    while True:
        # Ask the user what entry he wants to show, use q for exit
        key = console.input("[red](press 'q' to exit) >>> [/red]")
        if key == 'q':
            exit(0)
        else:
            try:
                # Throws if the key is not an integer
                val = ord(key)
                if val > 57 or val < 48:
                    return
                # String to int via conversion
                val = val - 48
                page = wikipedia.page(ls[val])
                
                # Print the results of the page
                console.print(Panel.fit("[bold yellow]"+page.url+"[/bold yellow]\n[bold magenta]"+page.title+"[/bold magenta]",title="url & title"))
                console.print(Panel.fit(page.content,title="content"))
                break
            except:
                console.print("[bold red]Try again, this time a number please.[/bold red]\n")


if __name__ == "__main__":
    console = Console()
    while True:
        query = console.input("[bold yellow](type 'quit' to exit) $> [/bold yellow]")
        # Exit if the user says so
        if query == 'quit':
            exit(0)
        process(query,console)
    


