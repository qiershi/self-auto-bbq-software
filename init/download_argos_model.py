import os

# 本地化

import argostranslate.package as pkg

print("========== 更新可用的包索引 ==========")
pkg.update_package_index()

print("========== 获取可用的包 ==========")
available_packages = pkg.get_available_packages()
for p in available_packages:
    print(f"{p}: \t{p.from_code} -> {p.to_code}")

print("========== 下载或加载所需的语言包 ==========")
def install_package(from_code, to_code):
    package_to_install = next(
            filter(
                lambda x: x.from_code == from_code and x.to_code == to_code, available_packages
                )
            )
    if package_to_install:
        print(f"下载并安装语言包: {package_to_install}")
        pkg.install_from_path(package_to_install.download())
    else:
        print(f"未找到从 {from_code} 到 {to_code} 的语言包")
        # 加载已安装的包
        installed_packages = pkg.get_installed_packages()
        required_package = next(
                filter(
                    lambda x: x.from_code == from_code and x.to_code == to_code, installed_packages
                    )
                )
        if not required_package:
            raise Exception(f"未找到或安装从 {from_code} 到 {to_code} 的语言包")


install_package("en", "zh")
install_package("ja", "en")
install_package("zh", "en")

