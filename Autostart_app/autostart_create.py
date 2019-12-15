import os
import argparse


def main():

    home = os.environ["HOME"]
    parser = argparse.ArgumentParser(description="Weather Reporter")

    parser.add_argument("-f", "--file", type=str, nargs=1,
                        metavar="file_name", default=None, help="file name")

    parser.add_argument("-s", "--script", type=str, nargs=1,
                        metavar="full_script_path", default=[1], help="full script path")

    parser.add_argument("-i", "--icon", type=str, nargs=1,
                        metavar="icon_name", default=[2], help="icon name")

    # parse the arguments from standard input
    args = vars(parser.parse_args())
    name = args['file'][0]
    icon_name = args['icon'][0]
    full_path= args['script'][0]
    script = os.path.basename(full_path)

    Path = os.path.dirname(full_path)
    command = "sh -c ./{} > ".format(script)+'"{}.log"'.format(name)+" 2>&1"
    icon = "./{}".format(icon_name)
    launcher = ["[Desktop Entry]",
                "Encoding=UTF-8",
                "Name=",
                "Path=",
                "Exec=",
                "Icon=",
                "Terminal=false",
                "Type=Application",
                "X-GNOME-Autostart-enabled=true",
                "X-GNOME-Autostart-Delay=0",
                ]
    dr = home + "/.config/autostart/"
    if not os.path.exists(dr):
        os.makedirs(dr)
    file = dr + name.lower() + ".desktop"
    if not os.path.exists(file):
        with open(file, "wt") as out:
            for l in launcher:
                l = l + name if l == "Name=" else l
                l = l + Path if l == "Path=" else l
                l = l + command if l == "Exec=" else l
                l = l + icon if l == "Icon=" else l
                out.write(l + "\n")
    else:
        print("file exists, choose another name")
        pass

if __name__ == "__main__":
	main()
