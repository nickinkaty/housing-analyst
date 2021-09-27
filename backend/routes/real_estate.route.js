import express from "express";

import {
  createRealEstates,
  getRealEstate,
  getRealEstateAnalyst,
} from "../controllers/real_estate.controller.js";

const router = express.Router();

// REAL ESTATE ROUTES
router
  .post("/", createRealEstates)
  .get("/", getRealEstate)
  .get("/analyst", getRealEstateAnalyst);
// router.post("/auth/signin", siginUser);
// router.get("/all", getRealEstate);

export default router;
