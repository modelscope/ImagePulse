import torch


class RandomPromptStyler:
    def __init__(self):
        self.styles = [
            {
                "name": "cinematic-diva",
                "name_zh": "电影歌星画风",
                "template": "UHD, 8K, ultra detailed, a cinematic photograph of {prompt}, beautiful lighting, great composition"
            },
            {
                "name": "Abstract Expressionism",
                "name_zh": "抽象表现主义",
                "template": "Abstract Expressionism Art, {prompt}, High contrast, minimalistic, colorful, stark, dramatic, expressionism"
            },
            {
                "name": "Academia",
                "name_zh": "学院风",
                "template": "Academia, {prompt}, preppy Ivy League style, stark, dramatic, chic boarding school, academia"
            },
            {
                "name": "Action Figure",
                "name_zh": "动作人偶",
                "template": "Action Figure, {prompt}, plastic collectable action figure, collectable toy action figure"
            },
            {
                "name": "Adorable 3D Character",
                "name_zh": "可爱的3D角色",
                "template": "Adorable 3D Character, {prompt}, 3D render, adorable character, 3D art"
            },
            {
                "name": "Adorable Kawaii",
                "name_zh": "可爱卡哇伊风格",
                "template": "Adorable Kawaii, {prompt}, pretty, cute, adorable, kawaii"
            },
            {
                "name": "Art Deco",
                "name_zh": "艺术装饰风格",
                "template": "Art Deco, {prompt}, sleek, geometric forms, art deco style"
            },
            {
                "name": "Art Nouveau",
                "name_zh": "新艺术风格",
                "template": "Art Nouveau, beautiful art, {prompt}, sleek, organic forms, long, sinuous, art nouveau style"
            },
            {
                "name": "Astral Aura",
                "name_zh": "星体光环",
                "template": "Astral Aura, {prompt}, astral, colorful aura, vibrant energy"
            },
            {
                "name": "Avant-garde",
                "name_zh": "先锋派",
                "template": "Avant-garde, {prompt}, unusual, experimental, avant-garde art"
            },
            {
                "name": "Baroque",
                "name_zh": "巴洛克风格",
                "template": "Baroque, {prompt}, dramatic, exuberant, grandeur, baroque art"
            },
            {
                "name": "Bauhaus-Style Poster",
                "name_zh": "包豪斯风格海报",
                "template": "Bauhaus-Style Poster, {prompt}, simple geometric shapes, clean lines, primary colors, Bauhaus-Style Poster"
            },
            {
                "name": "Blueprint Schematic Drawing",
                "name_zh": "蓝图原理图绘制",
                "template": "Blueprint Schematic Drawing, {prompt}, technical drawing, blueprint, schematic"
            },
            {
                "name": "Caricature",
                "name_zh": "漫画",
                "template": "Caricature, {prompt}, exaggerated, comical, caricature"
            },
            {
                "name": "Cel Shaded Art",
                "name_zh": "单色阴影艺术",
                "template": "Cel Shaded Art, {prompt}, 2D, flat color, toon shading, cel shaded style"
            },
            {
                "name": "Character Design Sheet",
                "name_zh": "角色设计图",
                "template": "Character Design Sheet, {prompt}, character reference sheet, character turn around"
            },
            {
                "name": "Classicism Art",
                "name_zh": "古典主义艺术",
                "template": "Classicism Art, {prompt}, inspired by Roman and Greek culture, clarity, harmonious, classicism art"
            },
            {
                "name": "Color Field Painting",
                "name_zh": "色域绘画",
                "template": "Color Field Painting, {prompt}, abstract, simple, geometic, color field painting style"
            },
            {
                "name": "Colored Pencil Art",
                "name_zh": "彩色铅笔艺术",
                "template": "Colored Pencil Art, {prompt}, colored pencil strokes, light color, visible paper texture, colored pencil art"
            },
            {
                "name": "Conceptual Art",
                "name_zh": "概念艺术",
                "template": "Conceptual Art, {prompt}, concept art"
            },
            {
                "name": "Constructivism",
                "name_zh": "结构主义",
                "template": "Constructivism Art, {prompt}, minimalistic, geometric forms, constructivism art"
            },
            {
                "name": "Cubism",
                "name_zh": "立体主义",
                "template": "Cubism Art, {prompt}, flat geometric forms, cubism art"
            },
            {
                "name": "Dadaism",
                "name_zh": "达达主义",
                "template": "Dadaism Art, {prompt}, satirical, nonsensical, dadaism art"
            },
            {
                "name": "Dark Fantasy",
                "name_zh": "黑暗幻想",
                "template": "Dark Fantasy Art, {prompt}, dark, moody, dark fantasy style"
            },
            {
                "name": "Dark Moody Atmosphere",
                "name_zh": "暗色忧郁氛围",
                "template": "Dark Moody Atmosphere, {prompt}, dramatic, mysterious, dark moody atmosphere"
            },
            {
                "name": "DMT Art Style",
                "name_zh": "DMT艺术风格",
                "template": "DMT Art Style, {prompt}, bright colors, surreal visuals, swirling patterns, DMT art style"
            },
            {
                "name": "Doodle Art",
                "name_zh": "涂鸦艺术",
                "template": "Doodle Art Style, {prompt}, drawing, freeform, swirling patterns, doodle art style"
            },
            {
                "name": "Double Exposure",
                "name_zh": "双重曝光",
                "template": "Double Exposure Style, {prompt}, double image ghost effect, image combination, double exposure style"
            },
            {
                "name": "Dripping Paint Splatter Art",
                "name_zh": "滴漆溅画艺术",
                "template": "Dripping Paint Splatter Art, {prompt}, dramatic, paint drips, splatters, dripping paint"
            },
            {
                "name": "Expressionism",
                "name_zh": "表现主义",
                "template": "Expressionism Art Style, {prompt}, movement, contrast, emotional, exaggerated forms, expressionism art style"
            },
            {
                "name": "Faded Polaroid Photo",
                "name_zh": "褪色的宝丽来照片",
                "template": "Faded Polaroid Photo, {prompt}, analog, old faded photo, old polaroid"
            },
            {
                "name": "Fauvism",
                "name_zh": "野兽派",
                "template": "Fauvism Art, {prompt}, painterly, bold colors, textured brushwork, fauvism art"
            },
            {
                "name": "Flat 2D Art",
                "name_zh": "扁平2D艺术",
                "template": "Flat 2D Art, {prompt}, simple flat color, 2-dimensional, Flat 2D Art Style"
            },
            {
                "name": "Fortnite Art Style",
                "name_zh": "堡垒之夜艺术风格",
                "template": "Fortnite Art Style, {prompt}, 3D cartoon, colorful, Fortnite Art Style"
            },
            {
                "name": "Futurism",
                "name_zh": "未来主义",
                "template": "Futurism Art Style, {prompt}, dynamic, dramatic, Futurism Art Style"
            },
            {
                "name": "Glitchcore",
                "name_zh": "故障核心",
                "template": "Glitchcore Art Style, {prompt}, dynamic, dramatic, distorted, vibrant colors, glitchcore art style"
            },
            {
                "name": "Glo-fi",
                "name_zh": "光环音乐风格",
                "template": "Glo-fi Art Style, {prompt}, dynamic, dramatic, vibrant colors, glo-fi art style"
            },
            {
                "name": "Googie Art Style",
                "name_zh": "古奇艺术风格",
                "template": "Googie Art Style, {prompt}, dynamic, dramatic, 1950's futurism, bold boomerang angles, Googie art style"
            },
            {
                "name": "Graffiti Art",
                "name_zh": "涂鸦艺术",
                "template": "Graffiti Art Style, {prompt}, dynamic, dramatic, vibrant colors, graffiti art style"
            },
            {
                "name": "Harlem Renaissance Art",
                "name_zh": "哈莱姆文艺复兴艺术",
                "template": "Harlem Renaissance Art Style, {prompt}, dynamic, dramatic, 1920s African American culture, Harlem Renaissance art style"
            },
            {
                "name": "High Fashion",
                "name_zh": "高级时装",
                "template": "High Fashion, {prompt}, dynamic, dramatic, haute couture, elegant, ornate clothing, High Fashion"
            },
            {
                "name": "Idyllic",
                "name_zh": "田园诗般的",
                "template": "Idyllic, {prompt}, peaceful, happy, pleasant, happy, harmonious, picturesque, charming"
            },
            {
                "name": "Impressionism",
                "name_zh": "印象主义",
                "template": "Impressionism, {prompt}, painterly, small brushstrokes, visible brushstrokes, impressionistic style"
            },
            {
                "name": "Infographic Drawing",
                "name_zh": "信息图表绘制",
                "template": "Infographic Drawing, {prompt}, diagram, infographic"
            },
            {
                "name": "Ink Dripping Drawing",
                "name_zh": "墨水滴画",
                "template": "Ink Dripping Drawing, {prompt}, ink drawing, dripping ink"
            },
            {
                "name": "Japanese Ink Drawing",
                "name_zh": "日本墨画",
                "template": "Japanese Ink Drawing, {prompt}, ink drawing, inkwash, Japanese Ink Drawing"
            },
            {
                "name": "Knolling Photography",
                "name_zh": "秩序拍摄",
                "template": "Knolling Photography, {prompt}, flat lay photography, object arrangment, knolling photography"
            },
            {
                "name": "Light Cheery Atmosphere",
                "name_zh": "轻快愉快的氛围",
                "template": "Light Cheery Atmosphere, {prompt}, happy, joyful, cheerful, carefree, gleeful, lighthearted, pleasant atmosphere"
            },
            {
                "name": "Logo Design",
                "name_zh": "标志设计",
                "template": "Logo Design, {prompt}, dynamic graphic art, vector art, minimalist, professional logo design"
            },
            {
                "name": "Luxurious Elegance",
                "name_zh": "奢华优雅",
                "template": "Luxurious Elegance, {prompt}, extravagant, ornate, designer, opulent, picturesque, lavish"
            },
            {
                "name": "Macro Photography",
                "name_zh": "微距摄影",
                "template": "Macro Photography, {prompt}, close-up, macro 100mm, macro photography"
            },
            {
                "name": "Mandola Art",
                "name_zh": "曼陀罗艺术",
                "template": "Mandola art style, {prompt}, complex, circular design, mandola"
            },
            {
                "name": "Marker Drawing",
                "name_zh": "马克笔绘图",
                "template": "Marker Drawing, {prompt}, bold marker lines, visibile paper texture, marker drawing"
            },
            {
                "name": "Medievalism",
                "name_zh": "中世纪主义",
                "template": "Medievalism, {prompt}, inspired by The Middle Ages, medieval art, elaborate patterns and decoration, Medievalism"
            },
            {
                "name": "Minimalism",
                "name_zh": "极简主义",
                "template": "Minimalism, {prompt}, abstract, simple geometic shapes, hard edges, sleek contours, Minimalism"
            },
            {
                "name": "Neo-Baroque",
                "name_zh": "新巴洛克",
                "template": "Neo-Baroque, {prompt}, ornate and elaborate, dynaimc, Neo-Baroque"
            },
            {
                "name": "Neo-Byzantine",
                "name_zh": "新拜占庭",
                "template": "Neo-Byzantine, {prompt}, grand decorative religious style, Orthodox Christian inspired, Neo-Byzantine"
            },
            {
                "name": "Neo-Futurism",
                "name_zh": "新未来主义",
                "template": "Neo-Futurism, {prompt}, high-tech, curves, spirals, flowing lines, idealistic future, Neo-Futurism"
            },
            {
                "name": "Neo-Impressionism",
                "name_zh": "新印象主义",
                "template": "Neo-Impressionism, {prompt}, tiny dabs of color, Pointillism, painterly, Neo-Impressionism"
            },
            {
                "name": "Neo-Rococo",
                "name_zh": "新洛可可",
                "template": "Neo-Rococo, {prompt}, curved forms, naturalistic ornamentation, elaborate, decorative, gaudy, Neo-Rococo"
            },
            {
                "name": "Neoclassicism",
                "name_zh": "新古典主义",
                "template": "Neoclassicism, {prompt}, ancient Rome and Greece inspired, idealic, sober colors, Neoclassicism"
            },
            {
                "name": "Op Art",
                "name_zh": "视觉艺术",
                "template": "Op Art, {prompt}, optical illusion, abstract, geometric pattern, impression of movement, Op Art"
            },
            {
                "name": "Ornate and Intricate",
                "name_zh": "华丽复杂",
                "template": "Ornate and Intricate, {prompt}, decorative, highly detailed, elaborate, ornate, intricate"
            },
            {
                "name": "Pencil Sketch Drawing",
                "name_zh": "铅笔素描",
                "template": "Pencil Sketch Drawing, {prompt}, black and white drawing, graphite drawing"
            },
            {
                "name": "Pop Art 2",
                "name_zh": "流行艺术",
                "template": "Pop Art, {prompt}, vivid colors, flat color, 2D, strong lines, Pop Art"
            },
            {
                "name": "Rococo",
                "name_zh": "洛可可",
                "template": "Rococo, {prompt}, flamboyant, pastel colors, curved lines, elaborate detail, Rococo"
            },
            {
                "name": "Silhouette Art",
                "name_zh": "剪影艺术",
                "template": "Silhouette Art, {prompt}, high contrast, well defined, Silhouette Art"
            },
            {
                "name": "Simple Vector Art",
                "name_zh": "简单矢量艺术",
                "template": "Simple Vector Art, {prompt}, 2D flat, simple shapes, minimalistic, professional graphic, flat color, high contrast, Simple Vector Art"
            },
            {
                "name": "Sketchup",
                "name_zh": "草图大师",
                "template": "Sketchup, {prompt}, CAD, professional design, Sketchup"
            },
            {
                "name": "Steampunk 2",
                "name_zh": "蒸汽朋克",
                "template": "Steampunk, {prompt}, retrofuturistic science fantasy, steam-powered tech, vintage industry, gears, neo-victorian, steampunk"
            },
            {
                "name": "Surrealism",
                "name_zh": "超现实主义",
                "template": "Surrealism, {prompt}, expressive, dramatic, organic lines and forms, dreamlike and mysterious, Surrealism"
            },
            {
                "name": "Suprematism",
                "name_zh": "至上主义",
                "template": "Suprematism, {prompt}, abstract, limited color palette, geometric forms, Suprematism"
            },
            {
                "name": "Terragen",
                "name_zh": "地形生成",
                "template": "Terragen, {prompt}, beautiful massive landscape, epic scenery, Terragen"
            },
            {
                "name": "Tranquil Relaxing Atmosphere",
                "name_zh": "宁静放松的氛围",
                "template": "Tranquil Relaxing Atmosphere, {prompt}, calming style, soothing colors, peaceful, idealic, Tranquil Relaxing Atmosphere"
            },
            {
                "name": "Sticker Designs",
                "name_zh": "贴纸设计",
                "template": "Vector Art Stickers, {prompt}, professional vector design, sticker designs, Sticker Sheet"
            },
            {
                "name": "Vibrant Rim Light",
                "name_zh": "生动的边缘光",
                "template": "Vibrant Rim Light, {prompt}, bright rim light, high contrast, bold edge light"
            },
            {
                "name": "Volumetric Lighting",
                "name_zh": "体积光照明",
                "template": "Volumetric Lighting, {prompt}, light depth, dramatic atmospheric lighting, Volumetric Lighting"
            },
            {
                "name": "Watercolor 2",
                "name_zh": "水彩",
                "template": "Watercolor style painting, {prompt}, visible paper texture, colorwash, watercolor"
            },
            {
                "name": "Whimsical and Playful",
                "name_zh": "异想天开和俏皮",
                "template": "Whimsical and Playful, {prompt}, imaginative, fantastical, bight colors, stylized, happy, Whimsical and Playful"
            },
            {
                "name": "Fooocus Sharp",
                "name_zh": "焦点锐化",
                "template": "cinematic still {prompt} . emotional, harmonious, vignette, 4k epic detailed, shot on kodak, 35mm photo, sharp focus, high budget, cinemascope, moody, epic, gorgeous, film grain, grainy"
            },
            {
                "name": "Fooocus Masterpiece",
                "name_zh": "焦点杰作",
                "template": "(masterpiece), (best quality), (ultra-detailed), {prompt}, illustration, disheveled hair, detailed eyes, perfect composition, moist skin, intricate details, earrings, by wlop"
            },
            {
                "name": "Fooocus Photograph",
                "name_zh": "焦点摄影",
                "template": "photograph {prompt}, 50mm . cinematic 4k epic detailed 4k epic detailed photograph shot on kodak detailed cinematic hbo dark moody, 35mm photo, grainy, vignette, vintage, Kodachrome, Lomography, stained, highly detailed, found footage"
            },
            {
                "name": "Fooocus Cinematic",
                "name_zh": "焦点电影",
                "template": "cinematic still {prompt} . emotional, harmonious, vignette, highly detailed, high budget, bokeh, cinemascope, moody, epic, gorgeous, film grain, grainy"
            },
            {
                "name": "mre-cinematic-dynamic",
                "name_zh": "MRE电影动态",
                "template": "epic cinematic shot of dynamic {prompt} in motion. main subject of high budget action movie. raw photo, motion blur. best quality, high resolution"
            },
            {
                "name": "mre-spontaneous-picture",
                "name_zh": "MRE自发图片",
                "template": "spontaneous picture of {prompt}, taken by talented amateur. best quality, high resolution. magical moment, natural look. simple but good looking"
            },
            {
                "name": "mre-artistic-vision",
                "name_zh": "MRE艺术视觉",
                "template": "powerful artistic vision of {prompt}. breathtaking masterpiece made by great artist. best quality, high resolution"
            },
            {
                "name": "mre-dark-dream",
                "name_zh": "MRE黑暗梦境",
                "template": "dark and unsettling dream showing {prompt}. best quality, high resolution. created by genius but depressed mad artist. grim beauty"
            },
            {
                "name": "mre-gloomy-art",
                "name_zh": "MRE忧郁艺术",
                "template": "astonishing gloomy art made mainly of shadows and lighting, forming {prompt}. masterful usage of lighting, shadows and chiaroscuro. made by black-hearted artist, drawing from darkness. best quality, high resolution"
            },
            {
                "name": "mre-bad-dream",
                "name_zh": "MRE恶梦",
                "template": "picture from really bad dream about terrifying {prompt}, true horror. bone-chilling vision. mad world that shouldn't exist. best quality, high resolution"
            },
            {
                "name": "mre-underground",
                "name_zh": "MRE地下",
                "template": "uncanny caliginous vision of {prompt}, created by remarkable underground artist. best quality, high resolution. raw and brutal art, careless but impressive style. inspired by darkness and chaos"
            },
            {
                "name": "mre-surreal-painting",
                "name_zh": "MRE超现实绘画",
                "template": "surreal painting representing strange vision of {prompt}. harmonious madness, synergy with chance. unique artstyle, mindbending art, magical surrealism. best quality, high resolution"
            },
            {
                "name": "mre-dynamic-illustration",
                "name_zh": "MRE动态插画",
                "template": "insanely dynamic illustration of {prompt}. best quality, high resolution. crazy artstyle, careless brushstrokes, emotional and fun"
            },
            {
                "name": "mre-undead-art",
                "name_zh": "MRE不死艺术",
                "template": "long forgotten art created by undead artist illustrating {prompt}, tribute to the death and decay. miserable art of the damned. wretched and decaying world. best quality, high resolution"
            },
            {
                "name": "mre-elemental-art",
                "name_zh": "MRE元素艺术",
                "template": "art illustrating insane amounts of raging elemental energy turning into {prompt}, avatar of elements. magical surrealism, wizardry. best quality, high resolution"
            },
            {
                "name": "mre-space-art",
                "name_zh": "MRE太空艺术",
                "template": "winner of inter-galactic art contest illustrating {prompt}, symbol of the interstellar singularity. best quality, high resolution. artstyle previously unseen in the whole galaxy"
            },
            {
                "name": "mre-ancient-illustration",
                "name_zh": "MRE古代插画",
                "template": "sublime ancient illustration of {prompt}, predating human civilization. crude and simple, but also surprisingly beautiful artwork, made by genius primeval artist. best quality, high resolution"
            },
            {
                "name": "mre-brave-art",
                "name_zh": "MRE勇敢艺术",
                "template": "brave, shocking, and brutally true art showing {prompt}. inspired by courage and unlimited creativity. truth found in chaos. best quality, high resolution"
            },
            {
                "name": "mre-heroic-fantasy",
                "name_zh": "MRE英雄幻想",
                "template": "heroic fantasy painting of {prompt}, in the dangerous fantasy world. airbrush over oil on canvas. best quality, high resolution"
            },
            {
                "name": "mre-dark-cyberpunk",
                "name_zh": "MRE黑暗赛博朋克",
                "template": "dark cyberpunk illustration of brutal {prompt} in a world without hope, ruled by ruthless criminal corporations. best quality, high resolution"
            },
            {
                "name": "mre-lyrical-geometry",
                "name_zh": "MRE抒情几何",
                "template": "geometric and lyrical abstraction painting presenting {prompt}. oil on metal. best quality, high resolution"
            },
            {
                "name": "mre-sumi-e-symbolic",
                "name_zh": "MRE墨绘象征",
                "template": "big long brushstrokes of deep black sumi-e turning into symbolic painting of {prompt}. master level raw art. best quality, high resolution"
            },
            {
                "name": "mre-sumi-e-detailed",
                "name_zh": "MRE墨绘精细",
                "template": "highly detailed black sumi-e painting of {prompt}. in-depth study of perfection, created by a master. best quality, high resolution"
            },
            {
                "name": "mre-manga",
                "name_zh": "MRE漫画",
                "template": "manga artwork presenting {prompt}. created by japanese manga artist. highly emotional. best quality, high resolution"
            },
            {
                "name": "mre-anime",
                "name_zh": "MRE动漫",
                "template": "anime artwork illustrating {prompt}. created by japanese anime studio. highly emotional. best quality, high resolution"
            },
            {
                "name": "mre-comic",
                "name_zh": "MRE漫画书",
                "template": "breathtaking illustration from adult comic book presenting {prompt}. fabulous artwork. best quality, high resolution"
            },
            {
                "name": "sai-3d-model",
                "name_zh": "SAI三维模型",
                "template": "professional 3d model {prompt} . octane render, highly detailed, volumetric, dramatic lighting"
            },
            {
                "name": "sai-analog film",
                "name_zh": "SAI模拟胶片",
                "template": "analog film photo {prompt} . faded film, desaturated, 35mm photo, grainy, vignette, vintage, Kodachrome, Lomography, stained, highly detailed, found footage"
            },
            {
                "name": "sai-anime",
                "name_zh": "SAI动漫",
                "template": "anime artwork {prompt} . anime style, key visual, vibrant, studio anime, highly detailed"
            },
            {
                "name": "sai-cinematic",
                "name_zh": "SAI电影",
                "template": "cinematic film still {prompt} . shallow depth of field, vignette, highly detailed, high budget, bokeh, cinemascope, moody, epic, gorgeous, film grain, grainy"
            },
            {
                "name": "sai-comic book",
                "name_zh": "SAI漫画书",
                "template": "comic {prompt} . graphic illustration, comic art, graphic novel art, vibrant, highly detailed"
            },
            {
                "name": "sai-craft clay",
                "name_zh": "SAI手工粘土",
                "template": "play-doh style {prompt} . sculpture, clay art, centered composition, Claymation"
            },
            {
                "name": "sai-digital art",
                "name_zh": "SAI数字艺术",
                "template": "concept art {prompt} . digital artwork, illustrative, painterly, matte painting, highly detailed"
            },
            {
                "name": "sai-enhance",
                "name_zh": "SAI增强",
                "template": "breathtaking {prompt} . award-winning, professional, highly detailed"
            },
            {
                "name": "sai-fantasy art",
                "name_zh": "SAI幻想艺术",
                "template": "ethereal fantasy concept art of  {prompt} . magnificent, celestial, ethereal, painterly, epic, majestic, magical, fantasy art, cover art, dreamy"
            },
            {
                "name": "sai-isometric",
                "name_zh": "SAI等距",
                "template": "isometric style {prompt} . vibrant, beautiful, crisp, detailed, ultra detailed, intricate"
            },
            {
                "name": "sai-line art",
                "name_zh": "SAI线条艺术",
                "template": "line art drawing {prompt} . professional, sleek, modern, minimalist, graphic, line art, vector graphics"
            },
            {
                "name": "sai-lowpoly",
                "name_zh": "SAI低多边形",
                "template": "low-poly style {prompt} . low-poly game art, polygon mesh, jagged, blocky, wireframe edges, centered composition"
            },
            {
                "name": "sai-neonpunk",
                "name_zh": "SAI霓虹朋克",
                "template": "neonpunk style {prompt} . cyberpunk, vaporwave, neon, vibes, vibrant, stunningly beautiful, crisp, detailed, sleek, ultramodern, magenta highlights, dark purple shadows, high contrast, cinematic, ultra detailed, intricate, professional"
            },
            {
                "name": "sai-origami",
                "name_zh": "SAI折纸",
                "template": "origami style {prompt} . paper art, pleated paper, folded, origami art, pleats, cut and fold, centered composition"
            },
            {
                "name": "sai-photographic",
                "name_zh": "SAI摄影",
                "template": "cinematic photo {prompt} . 35mm photograph, film, bokeh, professional, 4k, highly detailed"
            },
            {
                "name": "sai-pixel art",
                "name_zh": "SAI像素艺术",
                "template": "pixel-art {prompt} . low-res, blocky, pixel art style, 8-bit graphics"
            },
            {
                "name": "sai-texture",
                "name_zh": "SAI质地",
                "template": "texture {prompt} top down close-up"
            },
            {
                "name": "ads-advertising",
                "name_zh": "广告",
                "template": "advertising poster style {prompt} . Professional, modern, product-focused, commercial, eye-catching, highly detailed"
            },
            {
                "name": "ads-automotive",
                "name_zh": "汽车广告",
                "template": "automotive advertisement style {prompt} . sleek, dynamic, professional, commercial, vehicle-focused, high-resolution, highly detailed"
            },
            {
                "name": "ads-corporate",
                "name_zh": "企业广告",
                "template": "corporate branding style {prompt} . professional, clean, modern, sleek, minimalist, business-oriented, highly detailed"
            },
            {
                "name": "ads-fashion editorial",
                "name_zh": "时尚编辑",
                "template": "fashion editorial style {prompt} . high fashion, trendy, stylish, editorial, magazine style, professional, highly detailed"
            },
            {
                "name": "ads-food photography",
                "name_zh": "食品摄影",
                "template": "food photography style {prompt} . appetizing, professional, culinary, high-resolution, commercial, highly detailed"
            },
            {
                "name": "ads-gourmet food photography",
                "name_zh": "美食摄影",
                "template": "gourmet food photo of {prompt} . soft natural lighting, macro details, vibrant colors, fresh ingredients, glistening textures, bokeh background, styled plating, wooden tabletop, garnished, tantalizing, editorial quality"
            },
            {
                "name": "ads-luxury",
                "name_zh": "奢华广告",
                "template": "luxury product style {prompt} . elegant, sophisticated, high-end, luxurious, professional, highly detailed"
            },
            {
                "name": "ads-real estate",
                "name_zh": "房地产广告",
                "template": "real estate photography style {prompt} . professional, inviting, well-lit, high-resolution, property-focused, commercial, highly detailed"
            },
            {
                "name": "ads-retail",
                "name_zh": "零售广告",
                "template": "retail packaging style {prompt} . vibrant, enticing, commercial, product-focused, eye-catching, professional, highly detailed"
            },
            {
                "name": "artstyle-abstract",
                "name_zh": "抽象艺术风格",
                "template": "abstract style {prompt} . non-representational, colors and shapes, expression of feelings, imaginative, highly detailed"
            },
            {
                "name": "artstyle-abstract expressionism",
                "name_zh": "抽象表现主义",
                "template": "abstract expressionist painting {prompt} . energetic brushwork, bold colors, abstract forms, expressive, emotional"
            },
            {
                "name": "artstyle-art deco",
                "name_zh": "艺术装饰风格",
                "template": "art deco style {prompt} . geometric shapes, bold colors, luxurious, elegant, decorative, symmetrical, ornate, detailed"
            },
            {
                "name": "artstyle-art nouveau",
                "name_zh": "新艺术风格",
                "template": "art nouveau style {prompt} . elegant, decorative, curvilinear forms, nature-inspired, ornate, detailed"
            },
            {
                "name": "artstyle-constructivist",
                "name_zh": "构成主义",
                "template": "constructivist style {prompt} . geometric shapes, bold colors, dynamic composition, propaganda art style"
            },
            {
                "name": "artstyle-cubist",
                "name_zh": "立体主义",
                "template": "cubist artwork {prompt} . geometric shapes, abstract, innovative, revolutionary"
            },
            {
                "name": "artstyle-expressionist",
                "name_zh": "表现主义",
                "template": "expressionist {prompt} . raw, emotional, dynamic, distortion for emotional effect, vibrant, use of unusual colors, detailed"
            },
            {
                "name": "artstyle-graffiti",
                "name_zh": "涂鸦",
                "template": "graffiti style {prompt} . street art, vibrant, urban, detailed, tag, mural"
            },
            {
                "name": "artstyle-hyperrealism",
                "name_zh": "超现实主义",
                "template": "hyperrealistic art {prompt} . extremely high-resolution details, photographic, realism pushed to extreme, fine texture, incredibly lifelike"
            },
            {
                "name": "artstyle-impressionist",
                "name_zh": "印象主义",
                "template": "impressionist painting {prompt} . loose brushwork, vibrant color, light and shadow play, captures feeling over form"
            },
            {
                "name": "artstyle-pointillism",
                "name_zh": "点彩主义",
                "template": "pointillism style {prompt} . composed entirely of small, distinct dots of color, vibrant, highly detailed"
            },
            {
                "name": "artstyle-pop art",
                "name_zh": "波普艺术",
                "template": "pop Art style {prompt} . bright colors, bold outlines, popular culture themes, ironic or kitsch"
            },
            {
                "name": "artstyle-psychedelic",
                "name_zh": "迷幻艺术",
                "template": "psychedelic style {prompt} . vibrant colors, swirling patterns, abstract forms, surreal, trippy"
            },
            {
                "name": "artstyle-renaissance",
                "name_zh": "文艺复兴",
                "template": "renaissance style {prompt} . realistic, perspective, light and shadow, religious or mythological themes, highly detailed"
            },
            {
                "name": "artstyle-steampunk",
                "name_zh": "蒸汽朋克",
                "template": "steampunk style {prompt} . antique, mechanical, brass and copper tones, gears, intricate, detailed"
            },
            {
                "name": "artstyle-surrealist",
                "name_zh": "超现实主义",
                "template": "surrealist art {prompt} . dreamlike, mysterious, provocative, symbolic, intricate, detailed"
            },
            {
                "name": "artstyle-typography",
                "name_zh": "排版艺术",
                "template": "typographic art {prompt} . stylized, intricate, detailed, artistic, text-based"
            },
            {
                "name": "artstyle-watercolor",
                "name_zh": "水彩艺术",
                "template": "watercolor painting {prompt} . vibrant, beautiful, painterly, detailed, textural, artistic"
            },
            {
                "name": "futuristic-biomechanical",
                "name_zh": "未来生物力学",
                "template": "biomechanical style {prompt} . blend of organic and mechanical elements, futuristic, cybernetic, detailed, intricate"
            },
            {
                "name": "futuristic-biomechanical cyberpunk",
                "name_zh": "未来生物力学赛博朋克",
                "template": "biomechanical cyberpunk {prompt} . cybernetics, human-machine fusion, dystopian, organic meets artificial, dark, intricate, highly detailed"
            },
            {
                "name": "futuristic-cybernetic",
                "name_zh": "未来赛博",
                "template": "cybernetic style {prompt} . futuristic, technological, cybernetic enhancements, robotics, artificial intelligence themes"
            },
            {
                "name": "futuristic-cybernetic robot",
                "name_zh": "未来机器人",
                "template": "cybernetic robot {prompt} . android, AI, machine, metal, wires, tech, futuristic, highly detailed"
            },
            {
                "name": "futuristic-cyberpunk cityscape",
                "name_zh": "未来赛博朋克城市景观",
                "template": "cyberpunk cityscape {prompt} . neon lights, dark alleys, skyscrapers, futuristic, vibrant colors, high contrast, highly detailed"
            },
            {
                "name": "futuristic-futuristic",
                "name_zh": "未来主义",
                "template": "futuristic style {prompt} . sleek, modern, ultramodern, high tech, detailed"
            },
            {
                "name": "futuristic-retro cyberpunk",
                "name_zh": "未来复古赛博朋克",
                "template": "retro cyberpunk {prompt} . 80's inspired, synthwave, neon, vibrant, detailed, retro futurism"
            },
            {
                "name": "futuristic-retro futurism",
                "name_zh": "未来复古主义",
                "template": "retro-futuristic {prompt} . vintage sci-fi, 50s and 60s style, atomic age, vibrant, highly detailed"
            },
            {
                "name": "futuristic-sci-fi",
                "name_zh": "科幻未来主义",
                "template": "sci-fi style {prompt} . futuristic, technological, alien worlds, space themes, advanced civilizations"
            },
            {
                "name": "futuristic-vaporwave",
                "name_zh": "未来波",
                "template": "vaporwave style {prompt} . retro aesthetic, cyberpunk, vibrant, neon colors, vintage 80s and 90s style, highly detailed"
            },
            {
                "name": "game-bubble bobble",
                "name_zh": "游戏-泡泡龙",
                "template": "Bubble Bobble style {prompt} . 8-bit, cute, pixelated, fantasy, vibrant, reminiscent of Bubble Bobble game"
            },
            {
                "name": "game-cyberpunk game",
                "name_zh": "赛博朋克游戏",
                "template": "cyberpunk game style {prompt} . neon, dystopian, futuristic, digital, vibrant, detailed, high contrast, reminiscent of cyberpunk genre video games"
            },
            {
                "name": "game-fighting game",
                "name_zh": "格斗游戏",
                "template": "fighting game style {prompt} . dynamic, vibrant, action-packed, detailed character design, reminiscent of fighting video games"
            },
            {
                "name": "game-gta",
                "name_zh": "侠盗猎车手游戏",
                "template": "GTA-style artwork {prompt} . satirical, exaggerated, pop art style, vibrant colors, iconic characters, action-packed"
            },
            {
                "name": "game-mario",
                "name_zh": "马里奥游戏",
                "template": "Super Mario style {prompt} . vibrant, cute, cartoony, fantasy, playful, reminiscent of Super Mario series"
            },
            {
                "name": "game-minecraft",
                "name_zh": "我的世界游戏",
                "template": "Minecraft style {prompt} . blocky, pixelated, vibrant colors, recognizable characters and objects, game assets"
            },
            {
                "name": "game-pokemon",
                "name_zh": "宝可梦游戏",
                "template": "Pokémon style {prompt} . vibrant, cute, anime, fantasy, reminiscent of Pokémon series"
            },
            {
                "name": "game-retro arcade",
                "name_zh": "复古街机",
                "template": "retro arcade style {prompt} . 8-bit, pixelated, vibrant, classic video game, old school gaming, reminiscent of 80s and 90s arcade games"
            },
            {
                "name": "game-retro game",
                "name_zh": "复古游戏",
                "template": "retro game art {prompt} . 16-bit, vibrant colors, pixelated, nostalgic, charming, fun"
            },
            {
                "name": "game-rpg fantasy game",
                "name_zh": "角色扮演幻想游戏",
                "template": "role-playing game (RPG) style fantasy {prompt} . detailed, vibrant, immersive, reminiscent of high fantasy RPG games"
            },
            {
                "name": "game-strategy game",
                "name_zh": "策略游戏",
                "template": "strategy game style {prompt} . overhead view, detailed map, units, reminiscent of real-time strategy video games"
            },
            {
                "name": "game-streetfighter",
                "name_zh": "街头霸王游戏",
                "template": "Street Fighter style {prompt} . vibrant, dynamic, arcade, 2D fighting game, highly detailed, reminiscent of Street Fighter series"
            },
            {
                "name": "game-zelda",
                "name_zh": "塞尔达传说游戏",
                "template": "Legend of Zelda style {prompt} . vibrant, fantasy, detailed, epic, heroic, reminiscent of The Legend of Zelda series"
            },
            {
                "name": "misc-architectural",
                "name_zh": "建筑",
                "template": "architectural style {prompt} . clean lines, geometric shapes, minimalist, modern, architectural drawing, highly detailed"
            },
            {
                "name": "misc-disco",
                "name_zh": "迪斯科",
                "template": "disco-themed {prompt} . vibrant, groovy, retro 70s style, shiny disco balls, neon lights, dance floor, highly detailed"
            },
            {
                "name": "misc-dreamscape",
                "name_zh": "梦境",
                "template": "dreamscape {prompt} . surreal, ethereal, dreamy, mysterious, fantasy, highly detailed"
            },
            {
                "name": "misc-dystopian",
                "name_zh": "反乌托邦",
                "template": "dystopian style {prompt} . bleak, post-apocalyptic, somber, dramatic, highly detailed"
            },
            {
                "name": "misc-fairy tale",
                "name_zh": "童话故事",
                "template": "fairy tale {prompt} . magical, fantastical, enchanting, storybook style, highly detailed"
            },
            {
                "name": "misc-gothic",
                "name_zh": "哥特",
                "template": "gothic style {prompt} . dark, mysterious, haunting, dramatic, ornate, detailed"
            },
            {
                "name": "misc-grunge",
                "name_zh": "垃圾摇滚",
                "template": "grunge style {prompt} . textured, distressed, vintage, edgy, punk rock vibe, dirty, noisy"
            },
            {
                "name": "misc-horror",
                "name_zh": "恐怖",
                "template": "horror-themed {prompt} . eerie, unsettling, dark, spooky, suspenseful, grim, highly detailed"
            },
            {
                "name": "misc-kawaii",
                "name_zh": "卡哇伊",
                "template": "kawaii style {prompt} . cute, adorable, brightly colored, cheerful, anime influence, highly detailed"
            },
            {
                "name": "misc-lovecraftian",
                "name_zh": "克苏鲁神话",
                "template": "lovecraftian horror {prompt} . eldritch, cosmic horror, unknown, mysterious, surreal, highly detailed"
            },
            {
                "name": "misc-macabre",
                "name_zh": "恐怖的",
                "template": "macabre style {prompt} . dark, gothic, grim, haunting, highly detailed"
            },
            {
                "name": "misc-manga",
                "name_zh": "漫画",
                "template": "manga style {prompt} . vibrant, high-energy, detailed, iconic, Japanese comic style"
            },
            {
                "name": "misc-metropolis",
                "name_zh": "大都市",
                "template": "metropolis-themed {prompt} . urban, cityscape, skyscrapers, modern, futuristic, highly detailed"
            },
            {
                "name": "misc-minimalist",
                "name_zh": "极简主义",
                "template": "minimalist style {prompt} . simple, clean, uncluttered, modern, elegant"
            },
            {
                "name": "misc-monochrome",
                "name_zh": "单色",
                "template": "monochrome {prompt} . black and white, contrast, tone, texture, detailed"
            },
            {
                "name": "misc-nautical",
                "name_zh": "航海",
                "template": "nautical-themed {prompt} . sea, ocean, ships, maritime, beach, marine life, highly detailed"
            },
            {
                "name": "misc-space",
                "name_zh": "太空",
                "template": "space-themed {prompt} . cosmic, celestial, stars, galaxies, nebulas, planets, science fiction, highly detailed"
            },
            {
                "name": "misc-stained glass",
                "name_zh": "彩色玻璃",
                "template": "stained glass style {prompt} . vibrant, beautiful, translucent, intricate, detailed"
            },
            {
                "name": "misc-techwear fashion",
                "name_zh": "科技服饰",
                "template": "techwear fashion {prompt} . futuristic, cyberpunk, urban, tactical, sleek, dark, highly detailed"
            },
            {
                "name": "misc-tribal",
                "name_zh": "部落",
                "template": "tribal style {prompt} . indigenous, ethnic, traditional patterns, bold, natural colors, highly detailed"
            },
            {
                "name": "misc-zentangle",
                "name_zh": "禅绕画",
                "template": "zentangle {prompt} . intricate, abstract, monochrome, patterns, meditative, highly detailed"
            },
            {
                "name": "papercraft-collage",
                "name_zh": "纸艺拼贴",
                "template": "collage style {prompt} . mixed media, layered, textural, detailed, artistic"
            },
            {
                "name": "papercraft-flat papercut",
                "name_zh": "平面剪纸",
                "template": "flat papercut style {prompt} . silhouette, clean cuts, paper, sharp edges, minimalist, color block"
            },
            {
                "name": "papercraft-kirigami",
                "name_zh": "剪纸",
                "template": "kirigami representation of {prompt} . 3D, paper folding, paper cutting, Japanese, intricate, symmetrical, precision, clean lines"
            },
            {
                "name": "papercraft-paper mache",
                "name_zh": "纸浆塑型",
                "template": "paper mache representation of {prompt} . 3D, sculptural, textured, handmade, vibrant, fun"
            },
            {
                "name": "papercraft-paper quilling",
                "name_zh": "纸卷艺术",
                "template": "paper quilling art of {prompt} . intricate, delicate, curling, rolling, shaping, coiling, loops, 3D, dimensional, ornamental"
            },
            {
                "name": "papercraft-papercut collage",
                "name_zh": "剪纸拼贴",
                "template": "papercut collage of {prompt} . mixed media, textured paper, overlapping, asymmetrical, abstract, vibrant"
            },
            {
                "name": "papercraft-papercut shadow box",
                "name_zh": "剪纸影箱",
                "template": "3D papercut shadow box of {prompt} . layered, dimensional, depth, silhouette, shadow, papercut, handmade, high contrast"
            },
            {
                "name": "papercraft-stacked papercut",
                "name_zh": "堆叠剪纸",
                "template": "stacked papercut art of {prompt} . 3D, layered, dimensional, depth, precision cut, stacked layers, papercut, high contrast"
            },
            {
                "name": "papercraft-thick layered papercut",
                "name_zh": "厚层剪纸",
                "template": "thick layered papercut art of {prompt} . deep 3D, volumetric, dimensional, depth, thick paper, high stack, heavy texture, tangible layers"
            },
            {
                "name": "photo-alien",
                "name_zh": "异形",
                "template": "alien-themed {prompt} . extraterrestrial, cosmic, otherworldly, mysterious, sci-fi, highly detailed"
            },
            {
                "name": "photo-film noir",
                "name_zh": "黑色电影",
                "template": "film noir style {prompt} . monochrome, high contrast, dramatic shadows, 1940s style, mysterious, cinematic"
            },
            {
                "name": "photo-glamour",
                "name_zh": "魅力",
                "template": "glamorous photo {prompt} . high fashion, luxurious, extravagant, stylish, sensual, opulent, elegance, stunning beauty, professional, high contrast, detailed"
            },
            {
                "name": "photo-hdr",
                "name_zh": "高动态范围",
                "template": "HDR photo of {prompt} . High dynamic range, vivid, rich details, clear shadows and highlights, realistic, intense, enhanced contrast, highly detailed"
            },
            {
                "name": "photo-iphone photographic",
                "name_zh": "iPhone摄影",
                "template": "iphone photo {prompt} . large depth of field, deep depth of field, highly detailed"
            },
            {
                "name": "photo-long exposure",
                "name_zh": "长曝光",
                "template": "long exposure photo of {prompt} . Blurred motion, streaks of light, surreal, dreamy, ghosting effect, highly detailed"
            },
            {
                "name": "photo-neon noir",
                "name_zh": "霓虹黑色",
                "template": "neon noir {prompt} . cyberpunk, dark, rainy streets, neon signs, high contrast, low light, vibrant, highly detailed"
            },
            {
                "name": "photo-silhouette",
                "name_zh": "剪影",
                "template": "silhouette style {prompt} . high contrast, minimalistic, black and white, stark, dramatic"
            },
            {
                "name": "photo-tilt-shift",
                "name_zh": "倾斜移位",
                "template": "tilt-shift photo of {prompt} . selective focus, miniature effect, blurred background, highly detailed, vibrant, perspective control"
            }
        ]
        
    def __call__(self, prompt):
        style_id = torch.randint(0, len(self.styles), size=(1,)).tolist()[0]
        prompt = self.styles[style_id]["template"].format(prompt=prompt)
        return prompt
