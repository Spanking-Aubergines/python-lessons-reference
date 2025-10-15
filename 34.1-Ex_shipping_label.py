
def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print("")
    # for value in kwargs.values():
        # print(value, end=" ")
    print(f"{kwargs.get("street")}")
    if "apt" in kwargs:
        print(f"{kwargs.get("city")} {kwargs.get("country")} {kwargs.get("apt")}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get("city")} {kwargs.get("country")} {kwargs.get("pobox")}")
    else:
        print(f"{kwargs.get("city")} {kwargs.get("country")}")
    print(f"{kwargs.get("zip")}")

shipping_label("Dr.", "Doom", "Terrible", "I",
                street="123 street",
                city="Helsinky",
                country="Phoenicia",
                zip="31233-322",
                pobox="123123"
                )