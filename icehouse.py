from mcpi.minecraft import Minecraft
from mcpi import block

mc = Minecraft.create()

p = mc.player.getTilePos()

mc.setBlocks(p.x + 1, p.y, p.z + 1,
             p.x + 10, p.y + 5, p.z + 10,
             block.ICE)

mc.setBlocks(p.x + 2, p.y + 1, p.z + 2,
             p.x + 9, p.y + 4, p.z + 9,
             block.AIR)

mc.setBlocks(p.x + 5, p.y + 1, p.z + 1,
             p.x + 6, p.y + 3, p.z + 1,
             block.AIR)

mc.setBlocks(p.x + 2, p.y, p.z + 2,
             p.x + 9, p.y, p.z + 9,
             block.WOOL.id, 14)
