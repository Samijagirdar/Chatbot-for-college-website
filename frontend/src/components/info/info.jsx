import React from "react";
import "./info.css";

export default function Info(props) {
  return (
    <div className="flex flex-col min-h-screen">
      {/* Main Content */}
      <div className="flex-grow ml-10">
        <div className="container mx-auto px-4 py-6">
          <h1 className="text-2xl font-bold mb-6 text-white">
            BLDEA Chatbot - College Info &#128218;
          </h1>

          <div className="text-white rounded-lg shadow-md p-3">
            <h2 className="text-2xl font-bold">About BLDEA's Dr. P. G. Halakatti College of Engineering &#127891;</h2>
            <p>
              BLDEA's Dr. P. G. Halakatti College of Engineering is a prestigious institution located in Vijayapura, Karnataka. 
              BLDEA offers a wide range of programs in various disciplines, including engineering, management, and research.
            </p>
          </div>

          <div className="text-white rounded-lg shadow-md p-6">
            <h2 className="text-xl font-bold mb-4">Chatbot Features &#128172;</h2>
            <ul className="list-disc list-inside">
              <li>Instant answers to basic program queries &#128161;</li>
              <li>Customizable responses tailored to BLDEA Engineering college requirements &#128187;</li>
              <li>User-friendly interface for easy interaction &#128526;</li>
              <li>Natural Language Processing for better understanding &#128161;</li>
            </ul>
          </div>
        </div>
      </div>

      {/* Footer Section */}
      <div className="text-white py-4 text-center">
        <p>
          &#169; {new Date().getFullYear()} BLDEA's Dr. P. G. Halakatti College of Engineering &#127891;
        </p>
      </div>
    </div>
  );
}
