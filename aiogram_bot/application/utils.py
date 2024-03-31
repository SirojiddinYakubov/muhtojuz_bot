import aiohttp


async def get_application_by_id(application_id: int) -> dict | None:
    print(f"Appplication ID {application_id}")
    async with aiohttp.ClientSession(
            connector=aiohttp.TCPConnector(ssl=False)
    ) as session:
        async with session.get(f"https://954d-93-170-220-216.ngrok-free.app/api/applications/{application_id}/") as response:
            try:
                resp_json = await response.json()
            
                return resp_json
            except Exception as e:
                print("Error: ", e)
                return {}


def generate_progress_message(required_amount, earned_amount):
    """
    Calculates progress bar and text message based on amounts.

    Args:
        required_amount: The total amount required.
        earned_amount: The amount earned so far.

    Returns:
        A string containing the progress bar and text message.
    """

    # Calculate progress percentage
    progress_pct = int((earned_amount / required_amount) * 100)

    # Define progress bar characters
    full_block = "🟩"
    # empty_block = "◻️"
    empty_block = "🟥️"

    # Calculate filled and empty blocks based on progress
    filled_blocks = full_block * int(progress_pct / 10)
    empty_blocks = empty_block * (10 - int(progress_pct / 10))

    # Construct progress bar text
    progress_bar = f"{filled_blocks}{empty_blocks}"

    # Construct text message
    message_text = f"{progress_pct}% {progress_bar} 100%"
    return message_text
