import React from "react";
import { Button } from "../../components/ui/button";
import { ScrollArea } from "../../components/ui/scroll-area";

export const Main = () => {
  const partLabels = [
    { id: 1, name: "Part name", position: "top-6 left-[1193px]", lineImg: "https://c.animaapp.com/m8v5e0ao8GaXJy/img/line-11.svg", linePosition: "top-[46px] left-[1097px]" },
    { id: 2, name: "Part name", position: "top-[442px] left-[507px]", lineImg: "https://c.animaapp.com/m8v5e0ao8GaXJy/img/line-12.svg", linePosition: "top-[312px] left-[597px]" },
    { id: 3, name: "Part name", position: "top-[258px] left-[1193px]", lineImg: "https://c.animaapp.com/m8v5e0ao8GaXJy/img/line-13.svg", linePosition: "top-[217px] left-[941px]" },
    { id: 4, name: "Part name", position: "top-[462px] left-[1057px]", lineImg: "https://c.animaapp.com/m8v5e0ao8GaXJy/img/line-14.svg", linePosition: "top-[351px] left-[868px]" },
    { id: 5, name: "Part name", position: "top-0 left-[530px]", lineImg: "https://c.animaapp.com/m8v5e0ao8GaXJy/img/line-16.svg", linePosition: "top-[45px] left-[597px]" },
    { id: 6, name: "Part name", position: "top-[21px] left-[799px]", lineImg: "https://c.animaapp.com/m8v5e0ao8GaXJy/img/line-17.svg", linePosition: "top-[57px] left-[857px]" },
  ];

  const contactInfo = ["Social Media: -", "GitHub: -", "Gmail: -"];

  return (
    <ScrollArea className="h-screen w-full">
      <div className="bg-white w-full max-w-[1512px] mx-auto">
        {/* Hero Section */}
        <section className="relative min-h-screen w-full overflow-hidden px-4 py-8 md:px-8 lg:px-16 xl:px-0 xl:h-[902px]">
          <div className="relative w-full h-full flex flex-col items-center justify-center xl:block">
            <div className="text-center xl:absolute xl:w-[956px] xl:top-[83px] xl:left-[-165px] [-webkit-text-stroke:1px_#0000005c] font-normal text-transparent text-6xl sm:text-8xl md:text-9xl xl:text-[200px] tracking-[4.00px] [font-family:'Rethink_Sans',Helvetica] leading-tight xl:leading-[200px]">
              <span className="font-extrabold tracking-[8.00px]">BRICK</span>
              <br />
              <span className="font-semibold tracking-[8.00px]">BY</span>
            </div>

            <div className="hidden xl:block absolute top-0 left-[0px] [-webkit-text-stroke:1px_#ffffff] [font-family:'Rethink_Sans',Helvetica] font-extrabold text-[#00000024] text-[200px] text-center tracking-[4.00px] leading-[200px]">
              &quot;
            </div>

            <div className="hidden xl:block absolute bottom-0 left-[0px] [-webkit-text-stroke:1px_#ffffff] [font-family:'Rethink_Sans',Helvetica] font-extrabold text-[#00000024] text-[200px] text-center tracking-[4.00px] leading-[200px]">
              &quot;
            </div>

            <div className="mt-8 text-center xl:absolute xl:top-[102px] xl:left-[961px] [-webkit-text-stroke:1px_#ffffff] font-extrabold text-[#00000082] text-4xl sm:text-5xl xl:text-[70px] tracking-[1.40px] whitespace-nowrap [font-family:'Rethink_Sans',Helvetica] leading-tight xl:leading-[100px]">
              Brick
            </div>

            <div className="text-center xl:absolute xl:top-[190px] xl:left-[964px] text-[#00000082] text-4xl sm:text-5xl xl:text-[70px] tracking-[1.40px] whitespace-nowrap [-webkit-text-stroke:1px_#ffffff] [font-family:'Rethink_Sans',Helvetica] font-extrabold leading-tight xl:leading-[100px]">
              by
            </div>

            <div className="text-center xl:absolute xl:top-[255px] xl:left-[961px] [-webkit-text-stroke:1px_#ffffff] font-extrabold text-[#00000082] text-4xl sm:text-5xl xl:text-[70px] tracking-[1.40px] whitespace-nowrap [font-family:'Rethink_Sans',Helvetica] leading-tight xl:leading-[100px]">
              Brick
            </div>

            <div className="mt-8 text-center xl:absolute xl:w-[956px] xl:top-[503px] xl:left-[-165px] [-webkit-text-stroke:1px_#ffffff] font-normal text-[#00000024] text-6xl sm:text-8xl md:text-9xl xl:text-[200px] tracking-[4.00px] [font-family:'Rethink_Sans',Helvetica] leading-tight xl:leading-[200px]">
              <span className="font-extrabold tracking-[8.00px]">BRICK</span>
            </div>

            <img className="w-full max-w-[990px] h-auto mt-8 xl:absolute xl:w-[990px] xl:h-[566px] xl:top-[161px] xl:left-[-7px] object-cover" alt="LEGO Sorting Machine" src="https://c.animaapp.com/m8v5e0ao8GaXJy/img/p1-5.png" />

            <div className="mt-8 text-center xl:text-left xl:absolute xl:w-[382px] xl:top-[359px] xl:left-[961px] [font-family:'Roboto',Helvetica] font-normal text-[#0000005c] text-base xl:text-[17px] tracking-[0.34px] leading-[25px]">
              &#34;Say goodbye to the mess and hello to efficiency! Brick by Brick uses AI-powered sorting to organize your LEGO pieces by color, shape, and type—so you can focus on building, not searching.&#34;
            </div>

            <Button variant="outline" className="mt-8 xl:absolute xl:top-[516px] xl:left-[961px] h-[42px] px-4 border border-solid border-[#00000069] rounded-none [font-family:'Roboto',Helvetica] font-normal text-[#aeaeae] text-base xl:text-[17px] tracking-[0.34px]">
              View Project
            </Button>
          </div>
        </section>

        {/* Features Section */}
        <section className="relative min-h-screen w-full bg-[#f1f1f1] overflow-hidden px-4 py-8 md:px-8 lg:px-16 xl:px-0 xl:h-[895px]">
          <div className="hidden xl:block absolute w-[127px] h-[52px] top-[285px] left-[586px] border border-solid border-[#f2f1ec]" />

          <div className="hidden xl:block w-[990px] absolute bottom-[-60px] right-[-50px] font-normal text-transparent text-[300px] tracking-[6.00px] whitespace-nowrap [font-family:'Rethink_Sans',Helvetica] text-center leading-[300px]">
            <span className="font-extrabold text-white tracking-[18.00px]">BRICK</span>
          </div>

          <div className="mt-8 xl:absolute xl:w-[441px] xl:top-[409px] xl:left-[784px] [font-family:'Roboto',Helvetica] font-normal text-[#0000005c] text-base xl:text-[17px] tracking-[0.34px] leading-[25px]">
            &#34;Say goodbye to the mess and hello to efficiency! Brick by Brick uses AI-powered sorting to organize your LEGO pieces by color, shape, and type—so you can focus on building, not searching.&#34;
          </div>

          <Button variant="outline" className="mt-8 xl:absolute xl:h-[42px] xl:top-[530px] xl:left-[784px] px-4 border border-solid border-[#00000069] rounded-none [font-family:'Roboto',Helvetica] font-normal text-[#aeaeae] text-base xl:text-[17px] tracking-[0.34px]">
            Live Demo
          </Button>

          <img className="w-full max-w-[451px] h-auto mt-8 mx-auto xl:absolute xl:w-[451px] xl:h-[580px] xl:top-[132px] xl:left-[206px]" alt="LEGO Sorting Machine" src="https://c.animaapp.com/m8v5e0ao8GaXJy/img/p2-2.png" />

          <div className="mt-8 text-center xl:text-left xl:absolute xl:w-[536px] xl:top-[167px] xl:left-[567px] [font-family:'Rethink_Sans',Helvetica] font-extrabold text-[#aeaeae] text-3xl sm:text-4xl xl:text-[50px] tracking-[1.00px] leading-tight xl:leading-[45px]">
            &#34;AI-Powered Vision. Precision Sorting. Build Without Limits.&#34;
          </div>

          <div className="mt-8 text-center xl:text-left xl:absolute xl:w-44 xl:top-[358px] xl:left-[784px] [font-family:'Rethink_Sans',Helvetica] font-extrabold text-[#7a7a7a] text-2xl xl:text-3xl tracking-[0.60px] leading-tight xl:leading-[45px]">
            Title
          </div>
        </section>

        {/* Technical Section */}
        <section className="relative min-h-screen w-full overflow-hidden px-4 py-8 md:px-8 lg:px-16 xl:px-0 xl:h-[1173px]">
          <div className="relative xl:absolute xl:w-[1354px] xl:h-[587px] xl:top-[154px] xl:left-[-66px]">
            <div className="text-center xl:absolute xl:w-[1354px] xl:top-[223px] xl:left-0 [font-family:'Rethink_Sans',Helvetica] font-extrabold text-[#dbdbdb85] text-6xl sm:text-8xl md:text-9xl xl:text-[350px] tracking-[7.00px] leading-tight xl:leading-[350px] whitespace-nowrap">
              SORTER
            </div>

            <img className="w-full max-w-[794px] h-auto mt-8 mx-auto xl:absolute xl:w-[794px] xl:h-[573px] xl:top-[13px] xl:left-[426px]" alt="LEGO Sorting Machine" src="https://c.animaapp.com/m8v5e0ao8GaXJy/img/p1-4.png" />

            {partLabels.map((part) => (
              <React.Fragment key={part.id}>
                <div className={`hidden xl:block absolute w-[147px] ${part.position} [font-family:'Roboto',Helvetica] font-normal text-[#7a7a7ae0] text-[23px] tracking-[0.46px] leading-[25px] whitespace-nowrap`}>
                  {part.name}
                </div>
                <img className={`hidden xl:block absolute ${part.linePosition} ${part.id === 2 ? "w-28 h-[120px]" : part.id === 4 ? "w-[177px] h-[102px]" : part.id === 6 ? "w-[52px] h-[100px]" : "w-[86px] h-[22px]"}`} alt={`Line ${part.id}`} src={part.lineImg} />
              </React.Fragment>
            ))}
          </div>
        </section>

        {/* Footer */}
        <footer className="w-full min-h-[288px] bg-[#f1f1f1] flex items-center px-4 py-8 md:px-8 lg:px-16 xl:px-0 xl:h-72">
          <div className="w-full xl:ml-[152px]">
            <div className="[font-family:'Rethink_Sans',Helvetica] font-extrabold text-[#7a7a7a] text-2xl xl:text-[25px] tracking-[0.50px] leading-tight xl:leading-[45px] whitespace-nowrap mb-5">
              Contact Us
            </div>
            <div className="[font-family:'Roboto',Helvetica] font-normal text-[#0000005c] text-base xl:text-[17px] tracking-[0.34px] leading-[25px] mb-7">
              {contactInfo.map((info, index) => (
                <React.Fragment key={index}>
                  {info}
                  <br />
                </React.Fragment>
              ))}
            </div>
            <Button variant="outline" className="w-[151px] h-[43px] border border-solid border-[#7a7a7a] rounded-none [font-family:'Roboto',Helvetica] font-normal text-[#484646] text-base xl:text-[17px] tracking-[0.34px]">
              Leave Review
            </Button>
          </div>
        </footer>
      </div>
    </ScrollArea>
  );
};
