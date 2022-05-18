def get_lib_patches():
    return {
        "osx-arm64": [
            {
                "downloads": {
                    "artifact": {
                        "sha1": "f378f889797edd7df8d32272c06ca80a1b6b0f58",
                        "size": 13164,
                        "url": "https://libraries.minecraft.net/com/mojang/text2speech/1.11.3/text2speech-1.11.3.jar",
                    }
                },
                "name": "com.mojang:text2speech:1.11.3",
            },
            {
                "downloads": {
                    "artifact": {
                        "sha1": "369a83621e3c65496348491e533cb97fe5f2f37d",
                        "size": 91947,
                        "url": "https://github.com/MinecraftMachina/Java-Objective-C-Bridge/releases/download/1.1.0-mmachina.1/java-objc-bridge-1.1.jar",
                    }
                },
                "name": "ca.weblite:java-objc-bridge:1.1.0-mmachina.1",
            },
            {
                "downloads": {
                    "classifiers": {
                        "natives-osx": {
                            "sha1": "53f9c919f34d2ca9de8c51fc4e1e8282029a9232",
                            "size": 12186,
                            "url": "https://libraries.minecraft.net/net/java/jinput/jinput-platform/2.0.5/jinput-platform-2.0.5-natives-osx.jar",
                        }
                    }
                },
                "extract": {"exclude": ["META-INF/"]},
                "name": "net.java.jinput:jinput-platform:2.0.5",
                "natives": {"osx": "natives-osx"},
            },
            {
                "downloads": {
                    "artifact": {
                        "sha1": "39c7796b469a600f72380316f6b1f11db6c2c7c4",
                        "size": 208338,
                        "url": "https://libraries.minecraft.net/net/java/jinput/jinput/2.0.5/jinput-2.0.5.jar",
                    }
                },
                "name": "net.java.jinput:jinput:2.0.5",
            },
            {
                "downloads": {
                    "artifact": {
                        "sha1": "e12fe1fda814bd348c1579329c86943d2cd3c6a6",
                        "size": 7508,
                        "url": "https://libraries.minecraft.net/net/java/jutils/jutils/1.0.0/jutils-1.0.0.jar",
                    }
                },
                "name": "net.java.jutils:jutils:1.0.0",
            },
            {
                "downloads": {
                    "artifact": {
                        "sha1": "b04f3ee8f5e43fa3b162981b50bb72fe1acabb33",
                        "size": 22,
                        "url": "https://libraries.minecraft.net/org/lwjgl/lwjgl/lwjgl-platform/2.9.4-nightly-20150209/lwjgl-platform-2.9.4-nightly-20150209.jar",
                    },
                    "classifiers": {
                        "natives-osx": {
                            "sha1": "eff546c0b319d6ffc7a835652124c18089c67f36",
                            "size": 488316,
                            "url": "https://github.com/MinecraftMachina/lwjgl/releases/download/2.9.4-20150209-mmachina.2/lwjgl-platform-2.9.4-nightly-20150209-natives-osx.jar",
                        }
                    },
                },
                "extract": {"exclude": ["META-INF/"]},
                "name": "org.lwjgl.lwjgl:lwjgl-platform:2.9.4-nightly-20150209-mmachina.2",
                "natives": {"osx": "natives-osx"},
            },
            {
                "downloads": {
                    "artifact": {
                        "sha1": "697517568c68e78ae0b4544145af031c81082dfe",
                        "size": 1047168,
                        "url": "https://libraries.minecraft.net/org/lwjgl/lwjgl/lwjgl/2.9.4-nightly-20150209/lwjgl-2.9.4-nightly-20150209.jar",
                    }
                },
                "name": "org.lwjgl.lwjgl:lwjgl:2.9.4-nightly-20150209",
            },
            {
                "downloads": {
                    "artifact": {
                        "sha1": "d51a7c040a721d13efdfbd34f8b257b2df882ad0",
                        "size": 173887,
                        "url": "https://libraries.minecraft.net/org/lwjgl/lwjgl/lwjgl_util/2.9.4-nightly-20150209/lwjgl_util-2.9.4-nightly-20150209.jar",
                    }
                },
                "name": "org.lwjgl.lwjgl:lwjgl_util:2.9.4-nightly-20150209",
            },
            {
                "downloads": {
                    "artifact": {
                        "sha1": "e9a101bca4fa30d26b21b526ff28e7c2d8927f1b",
                        "size": 130128,
                        "url": "https://github.com/MinecraftMachina/lwjgl3/releases/download/3.3.1-mmachina.1/lwjgl-glfw.jar",
                    }
                },
                "name": "org.lwjgl:lwjgl-glfw:3.3.1-mmachina.1",
            },
            {
                "downloads": {
                    "artifact": {
                        "sha1": "e9a101bca4fa30d26b21b526ff28e7c2d8927f1b",
                        "size": 130128,
                        "url": "https://github.com/MinecraftMachina/lwjgl3/releases/download/3.3.1-mmachina.1/lwjgl-glfw.jar",
                    },
                    "classifiers": {
                        "natives-macos": {
                            "sha1": "71d793d0a5a42e3dfe78eb882abc2523a2c6b496",
                            "size": 129076,
                            "url": "https://github.com/MinecraftMachina/lwjgl3/releases/download/3.3.1-mmachina.1/lwjgl-glfw-natives-macos-arm64.jar",
                        }
                    },
                },
                "name": "org.lwjgl:lwjgl-glfw:3.3.1-mmachina.1",
                "natives": {"osx": "natives-macos"},
            },
            {
                "downloads": {
                    "artifact": {
                        "sha1": "4fb94224378d3588d52d2beb172f2eeafea2d546",
                        "size": 36976,
                        "url": "https://github.com/MinecraftMachina/lwjgl3/releases/download/3.3.1-mmachina.1/lwjgl-jemalloc.jar",
                    }
                },
                "name": "org.lwjgl:lwjgl-jemalloc:3.3.1-mmachina.1",
            },
            {
                "downloads": {
                    "artifact": {
                        "sha1": "4fb94224378d3588d52d2beb172f2eeafea2d546",
                        "size": 36976,
                        "url": "https://github.com/MinecraftMachina/lwjgl3/releases/download/3.3.1-mmachina.1/lwjgl-jemalloc.jar",
                    },
                    "classifiers": {
                        "natives-macos": {
                            "sha1": "b0be721188d2e7195798780b1c5fe7eafe8091c1",
                            "size": 103478,
                            "url": "https://github.com/MinecraftMachina/lwjgl3/releases/download/3.3.1-mmachina.1/lwjgl-jemalloc-natives-macos-arm64.jar",
                        }
                    },
                },
                "name": "org.lwjgl:lwjgl-jemalloc:3.3.1-mmachina.1",
                "natives": {"osx": "natives-macos"},
            },
            {
                "downloads": {
                    "artifact": {
                        "sha1": "d48e753d85916fc8a200ccddc709b36e3865cc4e",
                        "size": 88880,
                        "url": "https://github.com/MinecraftMachina/lwjgl3/releases/download/3.3.1-mmachina.1/lwjgl-openal.jar",
                    }
                },
                "name": "org.lwjgl:lwjgl-openal:3.3.1-mmachina.1",
            },
            {
                "downloads": {
                    "artifact": {
                        "sha1": "d48e753d85916fc8a200ccddc709b36e3865cc4e",
                        "size": 88880,
                        "url": "https://github.com/MinecraftMachina/lwjgl3/releases/download/3.3.1-mmachina.1/lwjgl-openal.jar",
                    },
                    "classifiers": {
                        "natives-macos": {
                            "sha1": "6b80fc0b982a0723b141e88859c42d6f71bd723f",
                            "size": 346131,
                            "url": "https://github.com/MinecraftMachina/lwjgl3/releases/download/3.3.1-mmachina.1/lwjgl-openal-natives-macos-arm64.jar",
                        }
                    },
                },
                "name": "org.lwjgl:lwjgl-openal:3.3.1-mmachina.1",
                "natives": {"osx": "natives-macos"},
            },
            {
                "downloads": {
                    "artifact": {
                        "sha1": "962c2a8d2a8cdd3b89de3d78d766ab5e2133c2f4",
                        "size": 929233,
                        "url": "https://github.com/MinecraftMachina/lwjgl3/releases/download/3.3.1-mmachina.1/lwjgl-opengl.jar",
                    }
                },
                "name": "org.lwjgl:lwjgl-opengl:3.3.1-mmachina.1",
            },
            {
                "downloads": {
                    "artifact": {
                        "sha1": "962c2a8d2a8cdd3b89de3d78d766ab5e2133c2f4",
                        "size": 929233,
                        "url": "https://github.com/MinecraftMachina/lwjgl3/releases/download/3.3.1-mmachina.1/lwjgl-opengl.jar",
                    },
                    "classifiers": {
                        "natives-macos": {
                            "sha1": "bb575058e0372f515587b5d2d04ff7db185f3ffe",
                            "size": 41667,
                            "url": "https://github.com/MinecraftMachina/lwjgl3/releases/download/3.3.1-mmachina.1/lwjgl-opengl-natives-macos-arm64.jar",
                        }
                    },
                },
                "name": "org.lwjgl:lwjgl-opengl:3.3.1-mmachina.1",
                "natives": {"osx": "natives-macos"},
            },
            {
                "downloads": {
                    "artifact": {
                        "sha1": "703e4b533e2542560e9f94d6d8bd148be1c1d572",
                        "size": 113273,
                        "url": "https://github.com/MinecraftMachina/lwjgl3/releases/download/3.3.1-mmachina.1/lwjgl-stb.jar",
                    }
                },
                "name": "org.lwjgl:lwjgl-stb:3.3.1-mmachina.1",
            },
            {
                "downloads": {
                    "artifact": {
                        "sha1": "703e4b533e2542560e9f94d6d8bd148be1c1d572",
                        "size": 113273,
                        "url": "https://github.com/MinecraftMachina/lwjgl3/releases/download/3.3.1-mmachina.1/lwjgl-stb.jar",
                    },
                    "classifiers": {
                        "natives-macos": {
                            "sha1": "98f0ad956c754723ef354d50057cc30417ef376a",
                            "size": 178409,
                            "url": "https://github.com/MinecraftMachina/lwjgl3/releases/download/3.3.1-mmachina.1/lwjgl-stb-natives-macos-arm64.jar",
                        }
                    },
                },
                "name": "org.lwjgl:lwjgl-stb:3.3.1-mmachina.1",
                "natives": {"osx": "natives-macos"},
            },
            {
                "downloads": {
                    "artifact": {
                        "sha1": "1203660b3131cbb8681b17ce6437412545be95e0",
                        "size": 6802,
                        "url": "https://github.com/MinecraftMachina/lwjgl3/releases/download/3.3.1-mmachina.1/lwjgl-tinyfd.jar",
                    }
                },
                "name": "org.lwjgl:lwjgl-tinyfd:3.3.1-mmachina.1",
            },
            {
                "downloads": {
                    "artifact": {
                        "sha1": "1203660b3131cbb8681b17ce6437412545be95e0",
                        "size": 6802,
                        "url": "https://github.com/MinecraftMachina/lwjgl3/releases/download/3.3.1-mmachina.1/lwjgl-tinyfd.jar",
                    },
                    "classifiers": {
                        "natives-macos": {
                            "sha1": "015b931a2daba8f0c317d84c9d14e8e98ae56e0c",
                            "size": 41384,
                            "url": "https://github.com/MinecraftMachina/lwjgl3/releases/download/3.3.1-mmachina.1/lwjgl-tinyfd-natives-macos-arm64.jar",
                        }
                    },
                },
                "name": "org.lwjgl:lwjgl-tinyfd:3.3.1-mmachina.1",
                "natives": {"osx": "natives-macos"},
            },
            {
                "downloads": {
                    "artifact": {
                        "sha1": "8e664dd69ad7bbcf2053da23efc7848e39e498db",
                        "size": 719038,
                        "url": "https://github.com/MinecraftMachina/lwjgl3/releases/download/3.3.1-mmachina.1/lwjgl.jar",
                    }
                },
                "name": "org.lwjgl:lwjgl:3.3.1-mmachina.1",
            },
            {
                "downloads": {
                    "artifact": {
                        "sha1": "8e664dd69ad7bbcf2053da23efc7848e39e498db",
                        "size": 719038,
                        "url": "https://github.com/MinecraftMachina/lwjgl3/releases/download/3.3.1-mmachina.1/lwjgl.jar",
                    },
                    "classifiers": {
                        "natives-macos": {
                            "sha1": "984df31fadaab86838877b112e5b4e4f68a00ccf",
                            "size": 42693,
                            "url": "https://github.com/MinecraftMachina/lwjgl3/releases/download/3.3.1-mmachina.1/lwjgl-natives-macos-arm64.jar",
                        }
                    },
                },
                "name": "org.lwjgl:lwjgl:3.3.1-mmachina.1",
                "natives": {"osx": "natives-macos"},
            },
        ]
    }
