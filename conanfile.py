import os
from conans import ConanFile, tools


class VmaConan(ConanFile):
    name = "vma"
    version = "2.3.0"
    license = "MIT"
    author = "GPUOpen"
    url = "https://github.com/GPUOpen-LibrariesAndSDKs/VulkanMemoryAllocator"
    description = "Easy to integrate Vulkan memory allocation library"
    no_copy_source = True

    def source(self):
        tools.get(f'{self.url}/archive/v{self.version}.tar.gz')

    def package(self):
        include_folder = os.path.join(
            self.source_folder, f'VulkanMemoryAllocator-{self.version}','src')
        self.copy(pattern='*.h', dst='include', src=include_folder)
        self.copy(pattern='*.natvis', dst='vs', src=include_folder)

    def package_id(self):
        self.info.header_only()
