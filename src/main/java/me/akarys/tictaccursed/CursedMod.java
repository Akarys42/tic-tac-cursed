package me.akarys.tictaccursed;

import net.minecraft.item.Item;
import net.minecraft.registry.Registries;
import net.minecraft.registry.Registry;
import net.minecraft.util.Identifier;
import org.quiltmc.loader.api.ModContainer;
import org.quiltmc.qsl.base.api.entrypoint.ModInitializer;

public class CursedMod implements ModInitializer {
	Item CROSS = new Item(new Item.Settings());
	Item CIRCLE = new Item(new Item.Settings());
	Item UNKNOWN = new Item(new Item.Settings());

	@Override
	public void onInitialize(ModContainer mod) {
		Registry.register(Registries.ITEM, new Identifier("tictaccursed", "cross"), CROSS);
		Registry.register(Registries.ITEM, new Identifier("tictaccursed", "circle"), CIRCLE);
		Registry.register(Registries.ITEM, new Identifier("tictaccursed", "unknown"), UNKNOWN);
	}
}
