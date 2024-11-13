CREATE TABLE "combined_active_program_codes" (
    "Grant_Activity_Code" TEXT  NOT NULL ,
    "Grant_Program_Name" TEXT  NOT NULL ,
    "HRSA_Program_Area_Name" TEXT  NOT NULL ,
    PRIMARY KEY (
        "Grant_Activity_Code"
    )
);

CREATE TABLE "combined_award_program_codes" (
    "Grant_Activity_Code" TEXT  NOT NULL ,
    "Grant_Program_Name" TEXT  NOT NULL ,
    "HRSA_Program_Area_Name" TEXT  NOT NULL ,
    PRIMARY KEY (
        "Grant_Activity_Code"
    )
);

CREATE TABLE "maternal_ehb_grantees" (
    "ID" INTEGER PRIMARY KEY,
    "Program_Area" TEXT  NOT NULL ,
    "Program_Name" TEXT  NOT NULL ,
    "Fiscal_Year" INT  NOT NULL ,
    "Activity_Code" TEXT  NOT NULL ,
    "Grant_Number" TEXT  NOT NULL ,
    "Grantee_Name" TEXT  NOT NULL ,
    "State" TEXT  NOT NULL ,
    "County" TEXT  NOT NULL ,
    "Congressional_District" TEXT  NOT NULL ,
    "Grantee_Class" TEXT  NOT NULL ,
    "Awardee_Amount" INT  NOT NULL ,
    "Grantee_Contact_Details" TEXT  NOT NULL
);

CREATE TABLE "maternal_ehb_2023" (
    "Grantee_Name" TEXT  NOT NULL ,
    "Grant_Number" TEXT  NOT NULL ,
    "HRSA_Program_Area" TEXT  NOT NULL ,
    "Program_Name" TEXT  NOT NULL ,
    "Activity_Code" TEXT  NOT NULL ,
    "Fiscal_Year" INT  NOT NULL ,
    "Financial_Assistance" REAL  NOT NULL ,
    "County" TEXT  NOT NULL ,
    "State" TEXT  NOT NULL ,
    "DUNS_Number" INT  NOT NULL ,
    "UEI_Number" TEXT  NOT NULL ,
    PRIMARY KEY (
        "Grant_Number"
    )
);

CREATE TABLE "maternal_ehb_active" (
    "ID" INTEGER PRIMARY KEY,
    "Award_Year" INT  NOT NULL ,
    "Grantee_Name" TEXT  NOT NULL ,
    "Grantee_Address" TEXT  NOT NULL ,
    "Grantee_City" TEXT  NOT NULL ,
    "Grantee_State_Abbreviation" TEXT  NOT NULL ,
    "Grantee_ZIP_Code" TEXT  NOT NULL ,
    "Grant_Activity_Code" TEXT  NOT NULL ,
    "Grant_Number" TEXT  NOT NULL ,
    "Grant_Serial_Number" INT  NOT NULL ,
    "Project_Period_Start_Date" DATE  NOT NULL ,
    "Grant_Project_Period_End_Date" DATE  NOT NULL ,
    "HRSA_Program_Area_Code" TEXT  NOT NULL ,
    "HRSA_Program_Area_Name" TEXT  NOT NULL ,
    "Grant_Program_Name" TEXT  NOT NULL ,
    "US_Congressional_Representative_Name" TEXT  NOT NULL ,
    "Complete_County_Name" TEXT  NOT NULL ,
    "Name_of_US_Senator_Number_One" TEXT  NOT NULL ,
    "Name_of_US_Senator_Number_Two" TEXT  NOT NULL ,
    "Data_Warehouse_Record_Create_Date" DATE  NOT NULL ,
    "Grantee_Type_Description" TEXT  NOT NULL ,
    "DUNS_Number" REAL  NOT NULL ,
    "Geocoding_Artifact_Address_Primary_X_Coordinate" REAL  NOT NULL ,
    "Geocoding_Artifact_Address_Primary_Y_Coordinate" REAL  NOT NULL ,
    FOREIGN KEY("Grant_Activity_Code") REFERENCES "combined_active_program_codes" ("Grant_Activity_Code")
);

CREATE TABLE "maternal_ehb_awarded" (
    "Award_Year" INT  NOT NULL ,
    "Financial_Assistance" REAL  NOT NULL ,
    "Grantee_Address" TEXT  NOT NULL ,
    "Grantee_City" TEXT  NOT NULL ,
    "Grantee_County_Description" TEXT  NOT NULL ,
    "Grantee_County_Name" TEXT  NOT NULL ,
    "Grantee_Name" TEXT  NOT NULL ,
    "Grantee_Region_Code" REAL  NOT NULL ,
    "HRSA_Region" TEXT  NOT NULL ,
    "Grantee_State_Abbreviation" TEXT  NOT NULL ,
    "State_Name" TEXT  NOT NULL ,
    "Grantee_ZIP_Code" INT  NOT NULL ,
    "Grant_Activity_Code" TEXT  NOT NULL ,
    "Grant_Number" TEXT  NOT NULL ,
    "Grant_Serial_Number" INT  NOT NULL ,
    "Project_Period_Start_Date" DATE  NOT NULL ,
    "Project_Period_Start_Date_Text_String" DATE  NOT NULL ,
    "Grant_Project_Period_End_Date" DATE  NOT NULL ,
    "Grant_Project_Period_End_Date_Text" DATE  NOT NULL ,
    "HRSA_Program_Area_Code" TEXT  NOT NULL ,
    "HRSA_Program_Area_Name" TEXT  NOT NULL ,
    "Complete_County_Name" TEXT  NOT NULL ,
    "Grant_Program_Name" TEXT  NOT NULL ,
    "Congressional_District_Name" TEXT  NOT NULL ,
    "Congressional_District_Number" INT  NOT NULL ,
    "HHS_Region_Number" INT  NOT NULL ,
    "US_Congressional_Representative_Name" TEXT  NOT NULL ,
    "State_and_County_Federal_Information_Processing_Standard_Code" INT  NOT NULL ,
    "State_FIPS_Code" INT  NOT NULL ,
    "Name_of_US_Senator_Number_One" TEXT  NOT NULL ,
    "Name_of_US_Senator_Number_Two" TEXT  NOT NULL ,
    "Grantee_Type_Description" TEXT  NOT NULL ,
    "DUNS_Number" INT  NOT NULL ,
    "Unique_Entity_Identifier" TEXT  NOT NULL ,
    "CCN" INT  NOT NULL ,
    "Geocoding_Artifact_Address_Primary_X_Coordinate" REAL  NOT NULL ,
    "Geocoding_Artifact_Address_Primary_Y_Coordinate" REAL  NOT NULL ,
    "Data_Warehouse_Record_Create_Date" DATE  NOT NULL ,
    "Data_Warehouse_Record_Create_Date_Text" DATE  NOT NULL ,
    PRIMARY KEY (
        "Grant_Serial_Number"
    ),
    FOREIGN KEY("Grant_Number") REFERENCES "maternal_ehb_grantees" ("Grant_Number")
);

CREATE TABLE "wic_states" (
    "ID" INTEGER PRIMARY KEY,
    "State_Indian_Tribe" TEXT  NOT NULL ,
    "FY2019" REAL  NOT NULL ,
    "FY2020" REAL  NOT NULL ,
    "FY2021" REAL  NOT NULL ,
    "FY2022" REAL  NOT NULL ,
    "FY2023" REAL  NOT NULL ,
    FOREIGN KEY("State_Indian_Tribe") REFERENCES "maternal_ehb_awarded" ("State_Name")
);

CREATE TABLE "wic_totals" (
    "ID" INTEGER PRIMARY KEY,
    "January_2023" REAL  NOT NULL ,
    "February_2023" REAL  NOT NULL ,
    "March_2023" REAL  NOT NULL ,
    "April_2023" REAL  NOT NULL ,
    "May_2023" REAL  NOT NULL ,
    "June_2023" REAL  NOT NULL ,
    "July_2023" REAL  NOT NULL ,
    "August_2023" REAL  NOT NULL ,
    "September_2023" REAL  NOT NULL ,
    "October_2022" REAL  NOT NULL ,
    "November_2022" REAL  NOT NULL ,
    "December_2022" REAL  NOT NULL ,
    "State_Agency_or_Indian_Tribal_Organization" TEXT  NOT NULL ,
    "Average_Participation" REAL  NOT NULL ,
    FOREIGN KEY("State_Agency_or_Indian_Tribal_Organization") REFERENCES "maternal_ehb_awarded" ("State_Name")
);

-- ALTER TABLE "maternal_ehb_active" ADD CONSTRAINT "fk_maternal_ehb_active_Grant_Activity_Code" FOREIGN KEY("Grant_Activity_Code")
-- REFERENCES "combined_active_program_codes" ("Grant_Activity_Code");

-- ALTER TABLE "maternal_ehb_awarded" ADD CONSTRAINT "fk_maternal_ehb_awarded_Grant_Number" FOREIGN KEY("Grant_Number")
-- REFERENCES "maternal_ehb_grantees" ("Grant_Number");

-- ALTER TABLE "wic_states" ADD CONSTRAINT "fk_wic_states_State-IndianTribe" FOREIGN KEY("State-IndianTribe")
-- REFERENCES "maternal_ehb_awarded" ("State_Name");

-- ALTER TABLE "wic_totals" ADD CONSTRAINT "fk_wic_totals_State_Agency_or_Indian_Tribal_Organization" FOREIGN KEY("State_Agency_or_Indian_Tribal_Organization")
-- REFERENCES "maternal_ehb_awarded" ("State_Name");

