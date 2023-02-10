async def m001_initial(db):
    """
    Initial nostradmin table.
    """
    await db.execute(
        f"""
        CREATE TABLE nostradmin.relays (
            id TEXT NOT NULL PRIMARY KEY,
            url TEXT NOT NULL,
            active BOOLEAN DEFAULT true
        );
    """
    )
