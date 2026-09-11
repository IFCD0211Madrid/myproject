def run(smb_path: str) -> tuple:
    # TODO
    # host, path = smb_path.split('/', 1)
    corte = smb_path.find('/',2)
    host = smb_path[2:corte]
    path = smb_path[corte:]
    return host, path


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
