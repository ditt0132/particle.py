# -*- coding: UTF-8 -*-

from PIL import Image
from os.path import exists as filex
import os


def getInput():
    print("입력 파일의 경로를 입력하세요")
    path = input("> ")
    if not filex(path):
        print("파일이 존재하지 않습니다. Enter 키를 눌러 프로그램을 종료해주세요")
        input()
        exit(1)
    else:
        return path


def getOutput():
    print("출력될 파일의 이름(.mcfunction 제외)룰 입력해주세요")
    path = input("> ") + ".mcfunction"
    if filex(path):
        print("파일이 존재합니다. 파일을 삭제해주세요. Enter 키를 눌러 프로그램을 종료해주세요")
        input()
        exit(1)
    else:
        return path


def process_image():
    original = Image.open(getInput())
    print("픽셀수(높이)를 입력해주세요. 현재 크기가 아니라 작게 만들 새 크기입니다")
    print("너무 큰 높이를 입력하면 마인크래프트가 크래쉬 나거나, 파티클 제한으로 인해 안보일 수도 있습니다")
    height = int(input("> "))
    if height > 100:
        print("이렇게 높은 숫자를 쓰는 것은 매우 위험할 수 있습니다!")
        print("실수로 실행시 월드를 날려먹을 수도 있죠")
        print("정말 괜찮다면, YES 를 입력해주세요")
        if not input("> ") == "YES":
            exit(0)
        else:
            pass
    ratio = original.width / original.height
    width = int(height * ratio)
    resized = original.resize((width, height))
    reversed_image = resized.transpose(Image.FLIP_LEFT_RIGHT).transpose(Image.FLIP_TOP_BOTTOM)
    with open(getOutput(), "a") as file:
        for y in range(height):
            for x in range(width):
                pixel = reversed_image.getpixel((x, y))
                file.write(
                    f"particle minecraft:dust {round(pixel[0] / 255, 5)} {round(pixel[1] / 255, 5)} "
                    f"{round(pixel[2] / 255, 5)} 0.5 ~{x / 10} ~{y / 10} ~ 0 0 0 1 0 force\n")
    resized.show()
    print("\x1b[4;32m성공!\x1b[0;0m")
    print("Enter 키를 눌러 나가세요.")


os.system("title 파티클 변환기")
process_image()