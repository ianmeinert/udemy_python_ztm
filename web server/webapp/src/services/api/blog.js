import Api from "../api"


export const getHome = async () => {
    try {
        const response = await Api.get("/home");
        return response.data;
    } catch (error) {
        console.error(error);
    }
};

export const getAbout = async () => {
    try {
        const response = await Api.get("/about");
        return response.data;
    } catch (error) {
        console.error(error);
    }
};

export const getResume = async () => {
    try {
        const response = await Api.get("/resume");
        return response.data;
    } catch (error) {
        console.error(error);
    }
}; 